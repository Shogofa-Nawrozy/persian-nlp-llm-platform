from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from nlp.tokenizer import tokenize_text
from nlp.pos_tagger import pos_tag_text
from nlp.ner_tagger import ner_tag_text
from nlp.mistral_utils import generate_with_mistral

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/tokenize', methods=['POST'])
def tokenize():
    data = request.json
    text = data.get('text', '')
    tokens = tokenize_text(text)
    return jsonify({'tokens': tokens})

@app.route('/pos-tag', methods=['POST'])
def pos_tag():
    data = request.json
    text = data.get('text', '')
    pos_tags = pos_tag_text(text)
    return jsonify({'pos_tags': pos_tags})

@app.route('/ner', methods=['POST'])
def ner():
    data = request.json
    text = data.get('text', '')
    ner_tags = ner_tag_text(text)
    return jsonify({'ner_tags': ner_tags})

@app.route('/grammar-correct', methods=['POST'])
def grammar_correct():
    text = request.json.get('text', '')
    prompt = f"متن زبان فارسی زیر را لطفاً فقط نسخه اصلاح‌شده گرامری آن را به زبان فارسی برگردان:\n{text}"
    corrected = generate_with_mistral(prompt)
    return jsonify({'corrected': corrected})

@app.route('/rephrase', methods=['POST'])
def rephrase():
    text = request.json.get('text', '')
    prompt = f"جمله زیر را ساده‌تر یا با جمله‌ای دیگر به زبان فارسی بازنویسی کن:\n{text}"
    rephrased = generate_with_mistral(prompt)
    return jsonify({'rephrased': rephrased})


if __name__ == '__main__':
    app.run(debug=True)
