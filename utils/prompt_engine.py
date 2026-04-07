import os
import re

# Style configuration: maps style name → descriptive keywords appended to every prompt
STYLE_DESCRIPTORS = {
    "Cinematic": "cinematic photography, dramatic lighting, movie still, 35mm film, shallow depth of field",
    "Watercolor": "watercolor painting, soft brushstrokes, pastel tones, artistic, hand-painted illustration",
    "Comic Book": "comic book art, bold outlines, vivid colors, halftone dots, superhero style, graphic novel",
    "Photorealistic": "photorealistic, DSLR photo, ultra-detailed, 8K resolution, natural lighting, documentary",
    "Oil Painting": "oil painting, impasto texture, rich colors, classical art, museum quality, renaissance style",
}

DEFAULT_STYLE = "Cinematic"


def _gemini_enhance(text: str, style: str) -> str:
    """Use Google Gemini API to craft a rich visual prompt."""
    try:
        import google.generativeai as genai
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            return None
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")
        style_desc = STYLE_DESCRIPTORS.get(style, STYLE_DESCRIPTORS[DEFAULT_STYLE])
        system_prompt = (
            f"You are an expert visual prompt engineer for AI image generation.\n"
            f"Convert the following sentence from a sales pitch narrative into a single, "
            f"richly detailed, visually imaginative image prompt.\n"
            f"The image must be rendered in this style: {style_desc}.\n"
            f"Return ONLY the image prompt — no explanations, no quotes, no markdown.\n\n"
            f"Sentence: {text}"
        )
        response = model.generate_content(system_prompt)
        result = response.text.strip()
        # Strip any accidental markdown code fences
        result = re.sub(r"^```.*?\n", "", result, flags=re.DOTALL)
        result = re.sub(r"\n```$", "", result.strip())
        return result if result else None
    except Exception:
        return None


def _template_enhance(text: str, style: str) -> str:
    """Fallback: template-based prompt when no API key is available."""
    style_desc = STYLE_DESCRIPTORS.get(style, STYLE_DESCRIPTORS[DEFAULT_STYLE])
    return (
        f"A visually compelling scene depicting: {text}. "
        f"Setting: professional environment with warm, inviting atmosphere. "
        f"Mood: inspiring and hopeful. Characters are diverse and engaged. "
        f"Style: {style_desc}. High detail, award-winning composition."
    )


def enhance_prompt(text: str, style: str = DEFAULT_STYLE) -> str:
    """
    Generate an enhanced image prompt for a given text segment.
    Tries Gemini API first; falls back to template if unavailable.
    """
    gemini_result = _gemini_enhance(text, style)
    if gemini_result:
        # Append consistent style descriptor for visual consistency across panels
        style_desc = STYLE_DESCRIPTORS.get(style, STYLE_DESCRIPTORS[DEFAULT_STYLE])
        return f"{gemini_result}, {style_desc}"
    return _template_enhance(text, style)