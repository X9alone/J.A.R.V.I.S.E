import speech_recognition as sr
import os
import sys
import pyttsx3
import webbrowser
engine = pyttsx3.init()

import openai

from dotenv import load_dotenv as ld

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    ld(dotenv_path)

openai.api_key = os.getenv("api_key")


def input_ai(task):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": task}])
    return completion


take = input("Який тип помічника ти хочеш? Обери голосовий (1) чи письмовий (2) ")


def talk(words):
    print(words)
    if take == "1":
        engine.say(words)
        engine.runAndWait()



talk("Hi, can i help you?")


def command():
    if take == "1":
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)

        try:
            # task = r.recognize_google(audio, language="en-EN").lower()
            task = r.recognize_google(audio, language="uk-UA").lower()
            print("ви проговорили: " + task)
        except sr.UnknownValueError:
            talk("ya was ne zrozumiw")
            task = command()
    else:
        task = input("Your task: ")

    return task


def make_something(task):
    # if "open site" in task:
    if "відкрий" and "сайт" in task:
        talk("відкриваю")
        url = "https://ituniver.com"
        webbrowser.open(url)


    elif "ім'я" and "твоє" in task:
        talk("My name`s JARVIS")


    elif "стоп" in task:
        talk("Goodbye")
        sys.exit()

    else:
        try:
            ai_response = input_ai(task).choices[0].message.content
            talk(ai_response)
        except openai.error.ServiceUnavailableError:
            talk("sorry,i am going to try again")
            try:
                ai_response = input_ai(task).choices[0].message.content
                talk(ai_response)
            except openai.error.ServiceUnavailableError:
                talk("sorry, can you give me new task?")

while True:
    make_something(task=command())
