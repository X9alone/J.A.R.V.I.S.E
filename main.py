import speech_recognition as sr
import os
import sys
import pyttsx3
engine = pyttsx3.init()



def talk(words):
    print(words)
    engine.say(words)
    engine.runAndWait()



talk("Hi, can i help you?")


def command():
    r = sr.Recognizer()
    with sr.Microphone as source:
        print("Say")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        task = r.recognize_google(audio, language="ua-UA"),lower()
        print("ви проговорили: " + task)
    except sr.UnknownValueError:
        talk("Я вас не зрозумів")
        task = command()

    return task


def make_something(task):
    if "відкрий сайт" in task:
        talk("відкриваю")
        url = "https://ituniver.com"
        webbrowser.open(url)


while True:
    make_something(task=command())
