# 🌐 Pitch Visualizer

This project is a 100% Free and Fast implementation of **The Pitch Visualizer**. It programmatically converts sales narratives into multi-panel visual storyboards without requiring API keys or heavy local GPU models.

---

## 🎬 How it Works
A local tool that converts sales narratives into multi-panel visual storyboards.

### Features
- **Narrative Segmentation**: Intelligent sentence splitting via NLTK (local).
- **Intelligent Prompt Enrichment**: A local expansion engine that transforms narrative text into rich visual prompts using style-specific descriptors.
- **Fast, Free Image Generation**: Powered by **Pollinations.AI**, allowing instant, keyless image generation in the background. 
- **Dynamic UI**: Panels appear in real-time as they are processed.
- **Offline Core Logic**: Segmentation and prompt enrichment run entirely on your CPU.

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

---

## 📁 Project Structure
- `app.py`: Unified server and routing logic.
- `utils/`: 
  - `prompt_engine.py`: Local intelligent keyword expansion.
  - `image_gen.py`: High-speed generation wrapper using Pollinations API.
  - `segment.py`: NLTK segmentation logic.
- `static/output/`: Local storage for generated storyboard panels.

---

## 🛠 Tech Stack
- **Python / Flask**
- **Pollinations.AI / Hugging Face Ecosystem**
- **NLTK**
