import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source)
    print("audio is captured")  ##audio is captured
    audio = recognizer.listen(source)

    try:
        AudioConvTotext = recognizer.recognize_google(audio)
        print("your speech" + AudioConvTotext)
    except Exception as e:
        print("Error" + str(e))









