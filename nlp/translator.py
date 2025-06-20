from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


model_name = "Helsinki-NLP/opus-mt-fa-en"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def translate_fa_to_en(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
    output_ids = model.generate(inputs["input_ids"], max_length=512)
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)
