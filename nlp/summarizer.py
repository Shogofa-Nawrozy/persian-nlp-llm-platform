#from transformers import AutoTokenizer, MT5ForConditionalGeneration

model_name = "nafisehNik/mt5-persian-summary"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = MT5ForConditionalGeneration.from_pretrained(model_name)

def summarize(text):
    input_ids = tokenizer.encode(text, return_tensors="pt", truncation=True, max_length=512)
    summary_ids = model.generate(input_ids, max_length=60, min_length=5, num_beams=4)
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)
