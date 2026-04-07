# 🌐 Local-First Global Challenge Hub

This project provides a robust implementation of **The Empathy Engine** and **The Pitch Visualizer**, fully refactored to run **100% locally**. No external APIs (Google Gemini, Pollinations, OpenAI, etc.) are used, ensuring total privacy and offline capability.

---

## 🎭 Challenge 1: The Empathy Engine
A local service that analysises source text for emotional sentiment and generates a modulated human-like voice.

### Local-First Features
- **Emotion Detection**: Classifies text into Positive, Negative, or Neutral using `vaderSentiment`.
- **Vocal Modulation**: Programmatically alters **Rate** and **Volume** based on emotion via `pyttsx3`.
- **No API Keys**: Works instantly out of the box.

---

## 🎬 Challenge 2: The Pitch Visualizer
A local tool that converts sales narratives into multi-panel visual storyboards using Hugging Face models.

### Local-First Features
- **Narrative Segmentation**: Intelligent sentence splitting via NLTK (local).
- **Intelligent Prompt Enrichment**: A local expansion engine that transforms narrative text into rich visual prompts using style-specific descriptors.
- **Local Image Generation**: Powered by **Hugging Face `diffusers`**. 
  - *Note*: Runs on CPU by default. Generation time is approximately 1-2 minutes per panel depending on hardware.
- **Dynamic UI**: Panels appear in real-time as they are processed locally.

---

## 🚀 Setup & Execution

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Application
```bash
python app.py
```
Visit **http://127.0.0.1:5000**. 

> **Important**: Upon first run, the app will download approximately 4GB of model weights for Stable Diffusion. Ensure you have a stable internet connection for the initial setup.

---

## 📁 Project Structure
- `app.py`: Unified server with local storage management.
- `utils/`: 100% local logic modules.
  - `prompt_engine.py`: Local intelligent keyword expansion.
  - `image_gen.py`: Local HF `diffusers` (CPU-optimized).
  - `segment.py`: NLTK segmentation.
  - `voice_gen.py`: pyttsx3 voice synthesis.
- `static/output/`: Local storage for generated storyboard panels.

---

## 🛠 Tech Stack
- **Python / Flask**
- **Hugging Face Diffusers** (Stable Diffusion v1.5)
- **VADER Sentiment**
- **pyttsx3**
- **NLTK**
- **Torch** (CPU / CUDA)
