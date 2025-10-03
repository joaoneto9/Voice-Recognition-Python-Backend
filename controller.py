from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["POST"])
def transact_audio() -> str:
    
    if "audio" not in request.files:
        return jsonify({"'erro': 'Nenhum arquivo de áudio foi enviado'"}), 400
    
    audio = request.files["audio"]
    return f"enviei o audio {audio.filename}"