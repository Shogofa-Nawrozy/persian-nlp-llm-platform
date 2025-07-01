import stanza

# Load Persian pipeline once
nlp = stanza.Pipeline(lang='fa', processors='tokenize,mwt,pos,lemma')

def lemmatize_word(word):
    doc = nlp(word)
    if not doc.sentences:
        return {"lemma": word, "forms": []}

    lemma = doc.sentences[0].words[0].lemma
    root = lemma or word
    # Optional: Fake inflected forms for now
    forms = [f"می‌{root}", f"{root}م", f"{root}ی", f"{root}ند", f"{root}ه‌ام"]
    return {"lemma": root, "forms": forms}
