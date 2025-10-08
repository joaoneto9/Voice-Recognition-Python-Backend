from flask import Flask, request, jsonify 
from flask_cors import CORS 
from audio_utils.audio_operations import AudioOperations 

# ao definir HOST como 0.0.0.0, qualquer dispositivo que possa se conectar ao servidor (ip público ou não) pode usar esse serviço
HOST = '0.0.0.0' 
# definindo a porta 5000 como padrão da aplicação do lado do servidor
PORT = 5000 
# nome do campo que deve conter o arquivo de áudio
KEY_REQUEST_FIELD = "audio" 

# instanciando um objeto da classe Flask: o app
app = Flask(__name__) 
# liberando quaisquer acessos externos a essa aplicação (ambiente de desenvolvimento)
CORS(app) 

# criando endpoint para requisições POST
@app.route("/transcribe", methods=["POST"]) 
def get_audio_transcribed():

    # verificando se o campo 'audio' existe
    if KEY_REQUEST_FIELD not in request.files: 
        return jsonify({"Error": "No audio file detected!"}), 400

    # acessando arquivo de áudio
    audio_file = request.files[KEY_REQUEST_FIELD] 

    # verificando se o arquivo de áudio possui um nome válido
    if audio_file.name == "": 
        return jsonify({"Error": "Invalid name for audio file!"}), 400

    try:

        audio_op = AudioOperations() # criando um instância da classe de operações de áudio

        webm_audio_bytes = audio_op.get_file_bytes(audio_file) # obtendo bytes do arquivo de áudio .webm (oriundo da requisição HTTP)

        wav_audio_file_path = audio_op.convert_to_wav(webm_audio_bytes) # gerando arquivo .wav a partir dos bytes do arquivo .webm

        final_transcription = audio_op.transcribe_audio(wav_audio_file_path) # gerando transcrição do áudio em texto

        return jsonify({"text": final_transcription}), 200 # retornando o texto no formato JSON

    except Exception as e: # captura erros no processo
        print(f"LOG: ERROR WHILE PROCESSING: {e}")
        return jsonify({"Error": {e}}), 400

def run_app():
    app.run(host=HOST, port=PORT) # roda a aplicação, especificando HOST e porta
