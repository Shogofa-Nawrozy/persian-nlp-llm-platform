from flair.data import Sentence
from flair.models import SequenceTagger

# Load the Persian POS tagger from Flair
tagger = SequenceTagger.load("hamedkhaledi/persian-flair-pos")

def pos_tag_text(text):
    sentence = Sentence(text)
    tagger.predict(sentence)
    result = [(token.text, token.get_label("pos").value) for token in sentence]
    return result
