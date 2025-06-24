#from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "google/madlad400-3b-mt"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def translate(text, target_lang='en'):
    lang_tag = f"<2{target_lang}>"
    prefixed_text = f"{lang_tag} {text}"
    inputs = tokenizer(prefixed_text, return_tensors="pt", truncation=True, max_length=512)
    output_ids = model.generate(inputs["input_ids"], max_length=512)
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)

