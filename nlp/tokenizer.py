# tokenizer.py

from transformers import AutoTokenizer

def tokenize_text(text):
    tokenizer = AutoTokenizer.from_pretrained("HooshvareLab/bert-base-parsbert-uncased")
    tokens = tokenizer.tokenize(text)
    return tokens


