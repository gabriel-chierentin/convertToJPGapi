import os
from flask import Flask, request, send_file
from PIL import Image
import io

app = Flask(__name__)

@app.route('/')
def home():
    return 'funcionando!'

@app.route('/processar', methods=['POST'])
def processar():
    if 'file' not in request.files:
        return 'Nenhum arquivo enviado.', 400

    arquivo_entrada = request.files['file']
    if arquivo_entrada.filename == '':
        return 'Nenhum arquivo selecionado.', 400

    nome_arquivo_saida = os.path.splitext(arquivo_entrada.filename)[0] + '.jpg'

    image = Image.open(arquivo_entrada)
    image = image.convert('RGBA')
    image = image.convert('RGB')
    output = io.BytesIO()
    image.save(output, format='JPEG')
    output.seek(0)

    return send_file(
        output,
        as_attachment=True,
        download_name=nome_arquivo_saida,
        mimetype='image/jpeg'
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
