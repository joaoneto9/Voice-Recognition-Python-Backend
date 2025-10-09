from werkzeug.datastructures import FileStorage
import whisper
import os
import io
import tempfile
from pydub import AudioSegment


class AudioOperations():
    """Classe utiliária para operações envolvendo arquivos de áudio.

    Aqui, tem-se operações importantes para o funcionamento da aplicação 
    no lado do servidor.
    """

    def __init__(self) -> None:
        self.transcription_model = "small"
        self.language = "portuguese"
        self.model =  whisper.load_model(self.transcription_model) # modelo da LLM é carregado.

    def get_file_bytes(self, audio_file: FileStorage) -> io.BytesIO:
        """Retorna os bytes de um arquivo. Nesse caso, um arquivo de áudio.

        Args:
            audio_file: Arquivo de áudio de qual deseja-se extrair os bytes.

        Returns:
            audio_file_bytes: Bytes do arquivo. 
        """
        audio_file_bytes = io.BytesIO(audio_file.read())
        return audio_file_bytes

    def convert_to_wav(self, audio_file_bytes: io.BytesIO) -> str:
        """Converte um arquivo de áudio, a partir de seus bytes, em um arquivo
        de áudio no formato wav (.wav), retornando o path de um arquivo wav temporário.

        Args:
            audio_file_bytes: Bytes do arquivo a ser convertido.

        Returns:
            temp_file_path: Path do arquivo wav temporário.
        """

        audio_file_segment = AudioSegment.from_file(audio_file_bytes, format="webm")

        audio_wav_bytes = io.BytesIO()

        audio_file_segment.export(audio_wav_bytes, format="wav")

        audio_wav_bytes.seek(0)

        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_file:
            temp_file.write(audio_wav_bytes.read())
            temp_file_path = temp_file.name

        return temp_file_path

    def transcribe_audio(self, audio_file_path: str):
        """Transcreve o conteúdo de um arquivo de áudio em texto utilizando whisper.
        Além disso, o arquivo temporário é removido da memória.

        Args:
            audio_file_path: Path do arquivo de áudio a ser transcrito.

        Returns:
            audio_transcription: Transcrição do arquivo de áudio em texto.
        """
        
        result = self.model.transcribe(
            audio_file_path, # arquivo a ser transcrito em texto
            language = self.language, # idioma do áudio
            fp16=False # formato de representação númerica dos dados de áudio
        )

        os.remove(audio_file_path) # removendo arquivo temporário

        audio_transcription = result["text"]

        return audio_transcription
