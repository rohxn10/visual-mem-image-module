import json
import requests
from pathlib import Path

from .prompt_builder import build_prompt


COMFY_URL = "http://127.0.0.1:8188/prompt"


def generate_image(story_text: str, emotion: str):
    # Load exported ComfyUI API workflow
    workflow_path = Path(__file__).parent / "workflows" / "dreamshaper_base_api.json"

    with open(workflow_path, "r") as f:
        workflow = json.load(f)

    # Build prompt
    positive_prompt, negative_prompt = build_prompt(story_text, emotion)

    # 🔴 IMPORTANT: edit ONLY text fields
    for node_id, node in workflow.items():
        if node.get("class_type") == "CLIPTextEncode":
            text = node["inputs"]["text"]

            # Heuristic: your positive prompt is longer & descriptive
            if "blurry" in text or "low quality" in text:
                node["inputs"]["text"] = negative_prompt
            else:
                node["inputs"]["text"] = positive_prompt

    payload = {
        "prompt": workflow
    }

    response = requests.post(COMFY_URL, json=payload)

    if response.status_code != 200:
        print("Status:", response.status_code)
        print(response.text)
        raise RuntimeError("ComfyUI generation failed")

    print("✅ Image generation request sent successfully")
