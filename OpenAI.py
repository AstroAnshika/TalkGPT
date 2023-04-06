import openai as openai
import os
import json
import speech_recognition as sr
import pyttsx3

openai.organization = "org-9VjtZhxENKeVWDtZ3uzmCUF6"
openai.api_key = "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"
r = sr.Recognizer()
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

#question="how to use openai projects"

while(1):
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            question = r.recognize_google(audio2)
            question = question.lower()
            print(question)
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=question,
                temperature=0.9,
                max_tokens=150,
                top_p=1,
                frequency_penalty=0.0,
                presence_penalty=0.6,
                stop=[" Human:", " AI:"]
            )
            print(str(response["choices"][0]["text"]))
            SpeakText(str(response["choices"][0]["text"]))
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occurred")






