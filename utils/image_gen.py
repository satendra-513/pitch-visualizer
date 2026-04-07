import os
import requests
import uuid
from urllib.parse import quote

def generate_image(prompt: str, style: str = "Cinematic") -> str:
    """
    Generate an image using Pollinations.AI for fast, free generation.
    It returns the image directly in the response.
    """
    output_dir = os.path.join("static", "output")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    filename = f"story_{uuid.uuid4().hex[:8]}.png"
    filepath = os.path.join(output_dir, filename)

    print(f"[Fast Gen] Requesting fast, free image for: {prompt[:40]}...")
    
    encoded_prompt = quote(prompt)
    seed = uuid.uuid4().int % 100000 
    # Use Pollinations AI (free, no API key, fast)
    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?seed={seed}&width=512&height=384&nologo=true"
    
    try:
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            with open(filepath, 'wb') as f:
                f.write(response.content)
            return f"/get-image/{filename}"
        else:
            print(f"[Fast Gen] API Error: {response.status_code}")
            return "https://dummyimage.com/600x400/222/fff&text=Gen+Failed"
    except Exception as e:
        print(f"[Fast Gen] Download Error: {e}")
        return "https://dummyimage.com/600x400/222/fff&text=Network+Error"
