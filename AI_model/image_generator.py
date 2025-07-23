from together import Together
import os
from dotenv import load_dotenv
load_dotenv()

def generate_image(prompt: str) -> str:
    """Generates an image using the Together API and returns the base64 encoded image."""
    client = Together(api_key=os.getenv("TOGETHER_API_KEY"))
    response = client.images.generate(
        prompt=prompt,
        model="black-forest-labs/FLUX.1-schnell-Free",
        steps=1,
        n=1,
        width=512,
        height=512,
        seed=None,
        format="b64_json"
    )
    return response.data[0].url