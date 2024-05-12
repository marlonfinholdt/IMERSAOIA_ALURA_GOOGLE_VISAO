from flask import Flask, request, jsonify
from gemini import GeminiAPI

app = Flask(__name__)

gemini_api = GeminiAPI(api_key="SUA_CHAVE_API_GEMINI")

@app.route('/transcrever', methods=['POST'])
def transcrever():
    foto = request.files['foto'] # Acessa a foto enviada pelo frontend
    transcricao = gemini_api.transcrever_imagem(foto) # Substitua pela função da API do Gemini
    return jsonify({'transcricao': transcricao})

if __name__ == "__main__":
    app.run(debug=True)
