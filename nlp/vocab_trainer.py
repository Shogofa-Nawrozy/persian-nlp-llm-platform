#from transformers import pipeline

# Placeholder: later use a Persian-specific model
pos_pipeline = pipeline( model="HooshvareLab/bert-base-parsbert-uncased", aggregation_strategy="simple")


def find_usages(text):
    result = pos_pipeline(text)
    return [{"word": r["word"], "entity": r["entity_group"]} for r in result]
