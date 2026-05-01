# Placeholder Flask server (preencha com a versão completa)
from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/')
def index():
    return jsonify({"status":"LSF-Net backend placeholder"})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
