from aifc import Error
from flask import Flask, request, jsonify
from flask_cors import CORS
import io
from audio_utils.audio_transcribe import audio_transcription

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

    audio_bytes = io.BytesIO(audio.read())

    try:
        #audio_transcription_text = audio_transcription(audio_bytes)
        return jsonify({"text": "oi"})
    except Error as e:
        return jsonify({"erro": f"Erro: {e}"}), 400

def run_app():
    app.run(host='0.0.0.0', port=5000)
