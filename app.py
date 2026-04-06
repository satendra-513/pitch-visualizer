from flask import Flask, render_template, request
from utils.segment import segment_text
from utils.prompt_engine import enhance_prompt
from utils.image_gen import generate_image

import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/generate', methods=['POST'])
def generate():
    text = request.form.get("text")

    # Step 1: segmentation
    segments = segment_text(text)

    results = []

    for seg in segments:
        # Step 2: enhance prompt
        prompt = enhance_prompt(seg)

        # Step 3: generate image
        image_url = generate_image(prompt)

        results.append({
            "text": seg,
            "image": image_url
        })

    return render_template("result.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)