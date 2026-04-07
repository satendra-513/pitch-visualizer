# 🌐 Global Challenge Hub

This repository contains completions for two major AI challenges: **The Empathy Engine** and **The Pitch Visualizer**. Both are integrated into a single Flask application with a modern, glassmorphic UI.

---

## 🎭 Challenge 1: The Empathy Engine
A service that analysises source text for emotional sentiment and generates a modulated human-like voice.

### Features
- **Emotion Detection**: Classifies text into Positive, Negative, or Neutral using VADER.
- **Vocal Modulation**: Programmatically alters **Rate**, **Pitch**, and **Volume** based on emotion.
- **Audio Output**: Generates playable `.wav` files via `pyttsx3`.
- **Intensity Scaling**: Modulation degree varies with the detected sentiment strength.

### Usage
Run the app and navigate to the **Empathy Engine** tab. Type emotional text and click **Analyse & Speak**.

---

## 🎬 Challenge 2: The Pitch Visualizer
A tool that converts sales narratives into multi-panel visual storyboards.

### Features
- **Narrative Segmentation**: Intelligent sentence splitting via NLTK.
- **LLM Prompt Engineering**: Uses Google Gemini 1.5 Flash to refine text into visual prompts.
- **AI Image Generation**: Powered by Pollinations.AI (free, zero-config).
- **Dynamic UI**: Storyboard panels stream in one-by-one using SSE.
- **Visual Styles**: 5 curated artistic styles (Cinematic, Watercolor, Comic Book, etc.).

---

## 🚀 Setup & Execution

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Environment
Copy `.env.example` to `.env` and add your `GEMINI_API_KEY`:
```
GEMINI_API_KEY=your_key_here
```
> **Note**: The app works without a key using a template-based prompt fallback.

### 3. Run the Application
```bash
python app.py
```
Visit **http://127.0.0.1:5000** to access the hub.

---

## 📁 Project Structure
- `app.py`: Unified server for both challenges.
- `utils/`: Core logic modules.
  - `empathy_engine.py`: Sentiment & parameter mapping.
  - `voice_gen.py`: pyttsx3 voice synthesis.
  - `segment.py`: NLTK narrative segmentation.
  - `prompt_engine.py`: Gemini LLM logic.
  - `image_gen.py`: Pollinations.AI API wrapper.
- `templates/`: HTML5 UIs (Pitch Visualizer & Empathy Engine).

---

## 🛠 Tech Stack
- **Python / Flask**
- **NLTK** (Segmentation)
- **VADER Sentiment** (Emotion)
- **pyttsx3** (TTS)
- **Google Gemini** (LLM)
- **Pollinations.AI** (Image Gen)
