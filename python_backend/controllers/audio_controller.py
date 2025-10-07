from flask import Flask, request, jsonify
from flask_cors import CORS
from audio_utils.audio_operations import AudioOperations

HOST = '0.0.0.0'
PORT = 5000
KEY_REQUEST_FIELD = "audio"

app = Flask(__name__)
CORS(app)

@app.route("/transcribe", methods=["GET"])
def get_req():
    return "opa"

@app.route("/transcribe", methods=["POST"])
def get_audio_transcribed():

    if KEY_REQUEST_FIELD not in request.files:
        return jsonify({"Error": "No audio file detected!"}), 400

    audio_file = request.files[KEY_REQUEST_FIELD]

    if audio_file.name == "":
        return jsonify({"Error": "Invalid name for audio file!"}), 400

    try:

        audio_op = AudioOperations()

        wav_audio_file_path = audio_op.convert_to_wav(audio_op.get_file_bytes(audio_file))

        final_transcription = audio_op.transcribe_audio(wav_audio_file_path)

        return jsonify({"text": final_transcription}), 200

    except Exception as e:
        print(f"LOG: ERROR WHILE PROCESSING: {e}")
        return jsonify({"Error": {e}}), 400

def run_app():
    app.run(host=HOST, port=PORT)
