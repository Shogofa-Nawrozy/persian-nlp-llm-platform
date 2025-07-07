from flask import Flask, request, session, jsonify, render_template
from flask_cors import CORS
from flask import send_from_directory

from pymongo import MongoClient
from bson.objectid import ObjectId
import os
from db.init_db import initialize_if_needed
import requests

# from nlp.pos_tagger import pos_tag_text
# from nlp.summarizer import summarize
# from nlp.grammar_corrector import correct_grammar
# from nlp.translator import translate_fa_to_en
# from nlp.vocab_trainer import find_usages

app = Flask(__name__)

# Call this once before starting the server
initialize_if_needed()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://nlp-mongo:27017/")
client = MongoClient(MONGO_URI)
db = client['daribrain']


# Replace this with your actual ngrok URL from Colab
COLAB_API_BASE = "https://8579-35-194-81-52.ngrok-free.app"

app = Flask(__name__)
CORS(app)

# ===== HTML Pages =====
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

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


# ===== Notebook Routes =====
@app.route('/daribrain')
def notebook():
    return render_template('/daribrain/main.html')


@app.route('/daribrain/vocab')
def vocab_book():
    # Example MongoDB or list-based retrieval
    # user_id = session.get('user_id')
    # vocab_items = db.vocab.find({"user_id": user_id})
    # return render_template("vocab_book.html", vocab_items=vocab_items)
    return render_template('/daribrain/vocab_book.html')


@app.route('/daribrain/notes', methods=['GET', 'POST'])
def add_note():
    # user_id = session.get('user_id')
    # if request.method == 'POST':
    #     note = {
    #         "user_id": user_id,
    #         "title": request.form['title'],
    #         "content": request.form['content']
    #     }
    #     db.notes.insert_one(note)
    #     return redirect(url_for('add_note'))

    # notes = db.notes.find({"user_id": user_id})
    # return render_template('notes.html', notes=notes)
    return render_template('/daribrain/notes.html')

# @app.route('/daribrain/notes/delete/<id>', methods=['POST'])
# def delete_note(id):
#     db.notes.delete_one({"_id": ObjectId(id)})
#     return redirect(url_for('add_note'))



@app.route('/daribrain/grammar', methods=['GET'])
def grammar_library():
    # Static list for now
    grammar_lessons = [
        {"id": 1, "title": "Present Simple", "description": "Used for regular actions and facts."},
        {"id": 2, "title": "Past Perfect", "description": "Actions completed before another past event."},
        {"id": 3, "title": "Future Tense", "description": "Describes actions that will happen."}
    ]
    return render_template("/daribrain/grammar_book.html", grammar_lessons=grammar_lessons)

# @app.route('/daribrain/grammar/save', methods=['POST'])
# def save_grammar():
#     user_id = session.get('user_id')
#     grammar = {
#         "user_id": user_id,
#         "title": request.form['title'],
#         "description": request.form['description']
#     }
#     db.grammar_notes.insert_one(grammar)
#     return jsonify({"success": True})

@app.route('/daribrain/my_grammar', methods=['GET'])
def my_grammar():
    # user_id = session.get('user_id')
    # saved_rules = list(db.grammar_notes.find({"user_id": user_id}))
    # return render_template("my_grammar.html", saved_rules=saved_rules)
    return render_template("/daribrain/my_grammar.html")



# ===== API Routes – Proxied to Colab =====
@app.route('/pos-tag', methods=['POST'])
def pos_tag():
    text = request.json.get('text', '')
    response = requests.post(f"{COLAB_API_BASE}/pos-tag", json={'text': text})
    return jsonify(response.json())


@app.route('/transliterate', methods=['POST'])
def transliterate_proxy():
    text = request.json.get('text', '')
    response = requests.post(f"{COLAB_API_BASE}/transliterate", json={'text': text})
    return jsonify(response.json())


@app.route('/vocab-usage', methods=['POST'])
def vocab_usage_route():
    text = request.json.get('text', '')
    response = requests.post(f"{COLAB_API_BASE}/vocab-usage", json={'text': text})
    return jsonify(response.json())




@app.route('/translate', methods=['POST'])
def translation_route():
    data = request.get_json()
    text = data.get('text', '')
    direction = data.get('direction', 'fa-en')

    # Forward the request to Colab model
    response = requests.post(f"{COLAB_API_BASE}/translate", json={
        'text': text,
        'direction': direction
    }, verify=False)

    return jsonify(response.json())




@app.route('/grammar-correct', methods=['POST'])
def grammar_correct():
    text = request.json.get('text', '').strip()

    if not text:
        return jsonify({'corrected': None, 'error': '⚠️ No text provided.'}), 400

    try:
        response = requests.get(
            'https://openl.io/grammar-check',
            params={'text': text},
            timeout=10
        )
        data = response.json()

        if 'correction' in data:
            return jsonify({'corrected': data['correction']})
        else:
            return jsonify({'corrected': None, 'error': data.get('error', 'No correction returned')}), 500
    except Exception as e:
        return jsonify({'corrected': None, 'error': f'OpenL Grammar failed: {str(e)}'}), 500



@app.route('/summarize', methods=['POST'])
def do_summarize():
    text = request.json.get('text', '')
    response = requests.post(f"{COLAB_API_BASE}/summarize", json={'text': text},  verify=False)
    return jsonify(response.json())


@app.route('/daribrain/lemma_tree/<word>')
def proxy_lemma_tree(word):
    response = requests.get(f"{COLAB_API_BASE}/daribrain/lemma_tree/{word}")
    return jsonify(response.json())



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
