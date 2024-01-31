#!/usr/bin/python3

import pyttsx3
speech = pyttsx3.init()
#print(speech.proxy._driver)
# <pyttsx3.drivers.sapi5.SAPI5Driver object at 0x000002623D70B7C0>
#speech.getProperty
voices = speech.getProperty('voices')
for voice in voices:
   speech.setProperty('voice', voice.id)
   print(voice.id, voice.name, voice)

   #speech.say('The quick brown fox jumped over the lazy dog.')
   speech.say('hello, how are you?')
   speech.runAndWait()

speech.stop()

# https://pyttsx3.readthedocs.io/en/latest/support.html
#  https://pyttsx3.readthedocs.io/en/latest/engine.html#pyttsx3.init

