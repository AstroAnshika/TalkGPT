import speech_recognition as sr
from gtts import gTTS
import pyttsx3
import os

str = " "
tts = gTTS(text="Go go bts", lang = 'en')
#str = tts.save('rec.mp3')
engine = pyttsx3.init()
engine.say(str)
engine.runAndWait()

