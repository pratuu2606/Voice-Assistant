import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import random
import pyjokes

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning")
    elif hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am your voice assistant. How can I help you?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print("You said:", query)
    except:
        return "None"
    return query.lower()

# MAIN
wish()

while True:
    query = take_command()

    # Open websites
    if 'youtube' in query:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif 'google' in query:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif 'github' in query:
        speak("Opening GitHub")
        webbrowser.open("https://github.com")

    # Time
    elif 'time' in query:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        speak("Current time is " + time)
        print(time)

    # Open apps (Windows example)
    elif 'notepad' in query:
        speak("Opening Notepad")
        os.system("notepad")

    elif 'calculator' in query:
        speak("Opening Calculator")
        os.system("calc")

    # Joke
    elif 'joke' in query:
        joke = pyjokes.get_joke()
        print(joke)
        speak(joke)

    # Random answer
    elif 'random number' in query:
        num = random.randint(1, 100)
        speak(f"Your random number is {num}")
        print(num)

    # Exit
    elif 'exit' in query:
        speak("Goodbye")
        break