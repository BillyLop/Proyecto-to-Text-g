import speech_recognition as sr
r = sr.Recognizer()

with sr.AudioFile("test.wav") as source:
    audio = r.record(source)
    try:
        s = r.recognize_google(audio)
        print("Text: "+s)
    except Exception as e:
        print("Exception: "+str(e))