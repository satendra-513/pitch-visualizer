import random

# Visual style descriptors for intelligent prompt expansion
STYLE_DESCRIPTORS = {
    "Cinematic": "cinematic photography, dramatic lighting, movie still, 35mm film, shallow depth of field, blockbuster aesthetic",
    "Watercolor": "watercolor painting, soft brushstrokes, pastel tones, artistic, wet-on-wet technique, delicate textures",
    "Comic Book": "comic book art, bold inks, vivid colors, halftone textures, superhero aesthetic, dynamic panel composition",
    "Photorealistic": "photorealistic, DSLR photo, ultra-detailed, 8K resolution, natural lighting, crisp focus, lifelike",
    "Oil Painting": "oil painting, thick impasto strokes, rich pigments, renaissance lighting, museum quality, textured canvas",
}

# General descriptors to make prompts more "intelligent" and visually rich
LIGHTING = ["golden hour", "soft studio lighting", "dramatic shadows", "volumetric fog", "ethereal glow"]
MOOD = ["inspiring", "hopeful", "professional", "vibrant", "peaceful", "determined"]
ENVIRONMENT = ["modern office", "scenic landscape", "bustling city", "futuristic lab", "collaborative workspace"]

def enhance_prompt(text: str, style: str = "Cinematic") -> str:
    """
    Enriches a simple narrative sentence into a visually descriptive image prompt.
    Works entirely locally without external APIs.
    """
    style_desc = STYLE_DESCRIPTORS.get(style, STYLE_DESCRIPTORS["Cinematic"])
    light = random.choice(LIGHTING)
    mood = random.choice(MOOD)
    env = random.choice(ENVIRONMENT)
    
    # Intelligent expansion via template and keyword injection
    # This transforms "The client was happy" into a much more descriptive prompt.
    expanded = (
        f"A visually compelling scene: {text}. "
        f"Set in a {env}. "
        f"Atmosphere is {mood} with {light}. "
        f"High detail, {style_desc}, sharp focus, professional composition."
    )
    return expanded