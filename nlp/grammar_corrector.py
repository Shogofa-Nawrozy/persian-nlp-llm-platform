# #from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# model_name = "m3hrdadfi/mt5-small-fa-wiki-grammar-correction"  
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# def correct_grammar(text):
#     input_text = f"grammar: {text}"
#     inputs = tokenizer(input_text, return_tensors="pt", truncation=True)
#     output = model.generate(inputs['input_ids'], max_length=512)
#     return tokenizer.decode(output[0], skip_special_tokens=True)
