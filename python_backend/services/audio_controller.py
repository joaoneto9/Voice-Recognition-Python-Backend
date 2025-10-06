from aifc import Error
from flask import Flask, request, jsonify
from flask_cors import CORS
import io
from audio_utils.audio_transcribe import audio_transcription
from pydub import AudioSegment
import tempfile
import os

app = Flask(__name__)
CORS(app)

@app.route("/transcribe", methods=["GET"])
def get_req():
    return "opa"

@app.route("/transcribe", methods=["POST"])
def transact_and_transcribe_audio():
    
    if "audio" not in request.files:
        return jsonify({"erro": "Nenhum arquivo de áudio foi enviado"}), 400
    
    audio = request.files["audio"]

    if audio.filename == "":
        return jsonify({"erro": "Nome de arquivo inválido"}), 400

    webm_audio_bytes = io.BytesIO(audio.read())

    try:

        audio_segment = AudioSegment.from_file(webm_audio_bytes, format="webm")

        wav_audio_bytes = io.BytesIO()

        audio_segment.export(wav_audio_bytes, format="wav")

        wav_audio_bytes.seek(0)

        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_wav_file:
            temp_wav_file.write(wav_audio_bytes.read())
            temp_wav_file_path = temp_wav_file.name

        audio_transcription_text = audio_transcription(temp_wav_file_path)

        os.remove(temp_wav_file_path)

        return jsonify({"text": audio_transcription_text})
    except Exception as e:
        print(f"LOG: ERRO DURANTE O PROCESSAMENTO: {e}")
        return jsonify({"erro": f"Erro: {e}"}), 400

def run_app():
    app.run(host='0.0.0.0', port=5000)
