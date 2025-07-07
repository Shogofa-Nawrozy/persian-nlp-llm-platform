from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from flask import Flask, request, jsonify

app = Flask(__name__)

model_name = "alirezamsh/small100"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Language tags for source and target
lang_prefixes = {
    "fa": "<fa>",
    "en": "<en>"
}
lang_targets = {
    "fa": "<2fa>",
    "en": "<2en>"
}

def translate(text, source_lang, target_lang):
    if source_lang not in lang_prefixes or target_lang not in lang_targets:
        return "[ERROR] Invalid language code"

    # Construct prompt like: "<en> <2fa> Heaven is under the feet of mothers"
    prompt = f"{lang_prefixes[source_lang]} {lang_targets[target_lang]} {text}"

    input_ids = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512).input_ids
    outputs = model.generate(input_ids, max_length=512, num_beams=4)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

@app.route("/translate", methods=["POST"])
def translate_route():
    data = request.get_json()
    text = data.get("text", "")
    direction = data.get("direction", "fa-en")

    try:
        source_lang, target_lang = direction.split("-")
        translated = translate(text, source_lang, target_lang)
        return jsonify({"translation": translated})
    except Exception as e:
        return jsonify({"error": f"Translation failed: {str(e)}"}), 500
