import whisper
import os
import io
import tempfile
from pydub import AudioSegment

class AudioOperations():

    def __init__(self):
        self.transcription_model = "small"
        self.language = "portuguese"

    def get_file_bytes(self, audio_file):
        return io.BytesIO(audio_file.read())

    def convert_to_wav(self, audio_file_bytes):

        audio_file_segment = AudioSegment.from_file(audio_file_bytes, format="webm")

        audio_wav_bytes = io.BytesIO()

        audio_file_segment.export(audio_wav_bytes, format="wav")

        audio_wav_bytes.seek(0)

        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_file:
            temp_file.write(audio_wav_bytes.read())
            temp_file_path = temp_file.name

        return temp_file_path

    def transcribe_audio(self, audio_file_path):

        model = whisper.load_model(self.transcription_model)

        result = model.transcribe(
            audio_file_path,
            language = self.language,
            fp16=False
        )

        os.remove(audio_file_path)

        return result["text"]
