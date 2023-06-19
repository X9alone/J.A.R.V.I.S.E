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