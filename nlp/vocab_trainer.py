from transformers import pipeline

# Placeholder: you can later use a Persian-specific model
pos_pipeline = pipeline("token-classification", model="HooshvareLab/bert-fa-base-ner", aggregation_strategy="simple")

def find_usages(text):
    result = pos_pipeline(text)
    return [{"word": r["word"], "entity": r["entity_group"]} for r in result]
