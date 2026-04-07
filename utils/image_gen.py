import urllib.parse
import requests
import time


def generate_image(prompt: str, style: str = "Cinematic") -> str:
    """
    Generate an image URL using Pollinations.AI free API.
    No API key required.
    Returns a direct image URL that can be embedded in HTML.
    """
    # Combine prompt with style for visual consistency
    full_prompt = f"{prompt.strip()}, {style.lower()} style, high quality, detailed"
    encoded = urllib.parse.quote(full_prompt)

    # Pollinations AI free image generation endpoint
    width, height = 768, 512
    url = f"https://image.pollinations.ai/prompt/{encoded}?width={width}&height={height}&nologo=true&seed={int(time.time()) % 10000}"
    return url