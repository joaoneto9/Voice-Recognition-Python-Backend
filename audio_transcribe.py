import speech_recognition as sr

r = sr.Recognizer()

with sr.AudioFile("gravacao.wav") as source:
    audio = r.record(source)

texto = r.recognize_google(audio, language="pt-BR")

print(texto)
