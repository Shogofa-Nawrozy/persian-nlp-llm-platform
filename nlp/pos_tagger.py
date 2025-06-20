import stanza

# Load Persian pipeline only once
nlp = stanza.Pipeline(lang='fa', processors='tokenize,mwt,pos,depparse', use_gpu=False)

def pos_tag_text(text):
    doc = nlp(text)
    results = []
    for sentence in doc.sentences:
        for word in sentence.words:
            results.append({
                "id": word.id,
                "text": word.text,
                "pos": word.upos,
                "head": word.head,
                "deprel": word.deprel
            })
    return results
