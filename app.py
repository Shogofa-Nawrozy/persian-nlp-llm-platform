from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from flask import send_from_directory

from nlp.pos_tagger import pos_tag_text
from nlp.summarizer import summarize
from nlp.grammar_corrector import correct_grammar
from nlp.translator import translate_fa_to_en
from nlp.vocab_trainer import find_usages


import requests

# Replace this with your actual ngrok URL from Colab
COLAB_API_BASE = "https://6432-34-86-69-3.ngrok-free.app"

app = Flask(__name__)
CORS(app)

# ===== HTML Pages =====
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/portfolio-details')
def portfolio_details():
    return render_template('portfolio-details.html')

@app.route('/services')
def services():
    return render_template('service-details.html')

@app.route('/pos_tagging')
def pos_tagging():
    return render_template('pos_tagging.html')

@app.route('/vocab_trainer')
def vocab_trainer():
    return render_template('vocab_trainer.html')

@app.route('/transelation')
def transelation():
    return render_template('transelation.html')

@app.route('/grammer_correction')
def grammer_correction():
    return render_template('grammer_correction.html')

@app.route('/summarization')
def summarization():
    return render_template('summarization.html')

@app.route('/text_to_speech')
def text_to_speech():
    return render_template('text_to_speech.html')

@app.route('/speech_to_text')
def speech_to_text():
    return render_template('speech_to_text.html')


# ===== API Routes – Proxied to Colab =====
@app.route('/pos-tag', methods=['POST'])
def pos_tag():
    text = request.json.get('text', '')
    response = requests.post(f"{COLAB_API_BASE}/pos-tag", json={'text': text})
    return jsonify(response.json())

@app.route('/vocab-usage', methods=['POST'])
def vocab_usage_route():
    text = request.json.get('text', '')
    response = requests.post(f"{COLAB_API_BASE}/vocab-usage", json={'text': text})
    return jsonify(response.json())

@app.route('/translate', methods=['POST'])
def translation_route():
    text = request.json.get('text', '')
    response = requests.post(f"{COLAB_API_BASE}/translate", json={'text': text})
    return jsonify(response.json())

# @app.route('/grammar-correct', methods=['POST'])
# def grammar_route():
#     text = request.json.get('text', '')
#     response = requests.post(f"{COLAB_API_BASE}/grammar-correct", json={'text': text})
#     return jsonify(response.json())

@app.route('/summarize', methods=['POST'])
def do_summarize():
    text = request.json.get('text', '')
    response = requests.post(f"{COLAB_API_BASE}/summarize", json={'text': text})
    return jsonify(response.json())


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
