import os
import json
from flask import Flask, render_template, request, Response, stream_with_context, send_from_directory
from dotenv import load_dotenv

from utils.segment import segment_text
from utils.prompt_engine import enhance_prompt, STYLE_DESCRIPTORS
from utils.image_gen import generate_image
from utils.empathy_engine import detect_emotion, get_voice_parameters
from utils.voice_gen import generate_voice

load_dotenv()

app = Flask(__name__)
app.config['AUDIO_FOLDER'] = os.path.join(app.root_path, 'static', 'audio')

STYLES = list(STYLE_DESCRIPTORS.keys())

# --- Basic Routes ---

@app.route('/')
def home():
    # Landing page is the Pitch Visualizer by default
    return render_template("index.html", styles=STYLES)

@app.route('/empathy')
def empathy_ui():
    return render_template("empathy.html")

# --- Pitch Visualizer Logic ---

@app.route('/generate-stream', methods=['POST'])
def generate_stream():
    """SSE endpoint for Pitch Visualizer."""
    text = request.form.get("text", "").strip()
    style = request.form.get("style", "Cinematic")

    def event_stream():
        if not text:
            yield f"data: {json.dumps({'error': 'No text provided'})}\n\n"
            return

        segments = segment_text(text)
        total = len(segments)
        yield f"data: {json.dumps({'type': 'start', 'total': total, 'style': style})}\n\n"

        for idx, seg in enumerate(segments):
            print(f"[Pitch] Panel {idx+1}/{total}: {seg[:30]}")
            prompt = enhance_prompt(seg, style)
            image_url = generate_image(prompt, style)
            panel = {
                "type": "panel",
                "index": idx,
                "total": total,
                "text": seg,
                "prompt": prompt,
                "image": image_url,
            }
            yield f"data: {json.dumps(panel)}\n\n"

        yield f"data: {json.dumps({'type': 'done', 'total': total})}\n\n"

    return Response(
        stream_with_context(event_stream()),
        content_type='text/event-stream',
        headers={'Cache-Control': 'no-cache', 'X-Accel-Buffering': 'no'}
    )

# --- Empathy Engine Logic ---

@app.route('/process-empathy', methods=['POST'])
def process_empathy():
    """API endpoint for Empathy Engine."""
    text = request.form.get("text", "").strip()
    if not text:
        return json.dumps({"error": "No text provided"}), 400
        
    emotion_data = detect_emotion(text)
    params = get_voice_parameters(emotion_data)
    audio_file = generate_voice(text, params, app.config['AUDIO_FOLDER'])
    
    if not audio_file:
        return json.dumps({"error": "Failed to generate voice"}), 500
        
    return json.dumps({
        "text": text,
        "emotion": emotion_data["emotion"],
        "intensity": round(emotion_data["intensity"], 2),
        "params": params,
        "audio_url": f"/audio/{audio_file}"
    })

@app.route('/audio/<filename>')
def serve_audio(filename):
    return send_from_directory(app.config['AUDIO_FOLDER'], filename)

if __name__ == "__main__":
    app.run(debug=True)