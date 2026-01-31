# image_module/emotion_visual_map.py

EMOTION_VISUAL_MAP = {
    "nostalgia": "warm colors, soft focus, golden hour lighting",
    "sadness": "cool tones, rain, muted colors",
    "joy": "bright lighting, vivid colors",
    "fear": "dark shadows, high contrast, moody lighting",
}

def emotion_to_visual(emotion: str) -> str:
    return EMOTION_VISUAL_MAP.get(emotion.lower(), "")
