from transformers import pipeline

pos_pipeline = pipeline(
    task="token-classification",
    model="HooshvareLab/bert-fa-base-uncased",
    aggregation_strategy="simple"  
)

def find_usages(text):
    result = pos_pipeline(text)
    return [{"word": r["word"], "entity": r["entity_group"]} for r in result]
