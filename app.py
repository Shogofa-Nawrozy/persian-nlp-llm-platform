from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from flask import send_from_directory
from nlp.pos_tagger import pos_tag_text
from nlp.summarizer import summarize

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def do_summarize():
    data = request.get_json()
    text = data.get('text', '')
    summary = summarize(text)
    return jsonify({'summary': summary})


@app.route('/portfolio-details')
def portfolio_details():
    return render_template('portfolio-details.html')

@app.route('/services')
def services():
    return render_template('service-details.html')

@app.route('/pos_tagging')
def pos_tagging():
    return render_template('pos_tagging.html')

@app.route('/pos-tag', methods=['POST'])
def pos_tag():
    data = request.json
    text = data.get('text', '')
    pos_tags = pos_tag_text(text)
    return jsonify({'tags': pos_tags})


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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
