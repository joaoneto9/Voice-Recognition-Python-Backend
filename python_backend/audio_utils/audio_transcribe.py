import speech_recognition as sr

PORTUGUESE = "pt-BR"

def audio_transcription(audio_file_path) -> str:
    r = sr.Recognizer()
    with sr.AudioFile(audio_file_path) as source:
        generated_audio = r.record(source)
    generated_text = r.recognize_google(generated_audio, language=PORTUGUESE)
    return generated_text
