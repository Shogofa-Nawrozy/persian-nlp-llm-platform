import stanza

nlp = stanza.Pipeline(lang='fa', processors='tokenize,pos,depparse')

def pos_tag_text(text):
    doc = nlp(text)
    result = []
    for sentence in doc.sentences:
        for word in sentence.words:
            result.append({
                'id': word.id,
                'text': word.text,
                'pos': word.xpos,
                'head': word.head,
                'deprel': word.deprel
            })
    return result
