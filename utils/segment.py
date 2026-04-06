import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

def segment_text(text):
    sentences = sent_tokenize(text)
    
    # minimum 3 segments
    return sentences[:5] if len(sentences) >= 3 else sentences