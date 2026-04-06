import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

def segment_text(text):
    sentences = text.split('. ')
    return [s.strip() for s in sentences if s]