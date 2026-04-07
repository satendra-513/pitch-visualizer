import nltk

# Download required tokenizer data silently
try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab', quiet=True)

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)


def segment_text(text: str) -> list[str]:
    """
    Segment input text into individual sentences using NLTK.
    Filters out empty or very short fragments (< 5 chars).
    Returns at least 1 segment even if tokenization yields nothing.
    """
    sentences = nltk.sent_tokenize(text.strip())
    cleaned = [s.strip() for s in sentences if len(s.strip()) >= 5]
    # Fallback: split by period if tokenizer returns nothing useful
    if not cleaned:
        cleaned = [s.strip() for s in text.split('.') if len(s.strip()) >= 5]
    return cleaned if cleaned else [text.strip()]