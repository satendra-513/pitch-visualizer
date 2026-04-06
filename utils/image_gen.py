import urllib.parse

def generate_image(text):
    safe_text = urllib.parse.quote(text[:40])
    return f"https://dummyimage.com/512x512/000/fff&text={safe_text}"