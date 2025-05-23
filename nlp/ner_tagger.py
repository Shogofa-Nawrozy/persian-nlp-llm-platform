from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

# Load the NER model from Hugging Face
model = AutoModelForTokenClassification.from_pretrained("HooshvareLab/bert-base-parsbert-ner-uncased")
tokenizer = AutoTokenizer.from_pretrained("HooshvareLab/bert-base-parsbert-ner-uncased")
ner_pipeline = pipeline("token-classification", model=model, tokenizer=tokenizer, aggregation_strategy="simple")

def ner_tag_text(text):
    results = ner_pipeline(text)
    return [(r['word'], r['entity_group']) for r in results if len(r['word']) > 2]
