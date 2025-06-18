from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "HooshvareLab/bert-fa-zwnj-wnli"  # Example placeholder
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def correct_grammar(text):
    prompt = f"متن زیر را از نظر نگارشی اصلاح کن:\n{text}"
    inputs = tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True)
    output_ids = model.generate(inputs["input_ids"], max_length=512, num_beams=4)
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)
