from .emotion_visual_map import EMOTION_VISUAL_MAP


def build_prompt(story_text: str, emotion: str):
    visual_hint = EMOTION_VISUAL_MAP.get(emotion, "")

    positive = f"{story_text}, {visual_hint}, cinematic, high quality, detailed"
    negative = "blurry, low quality, distorted, ugly"

    return positive, negative
