from together import Together
import os
import base64
from dotenv import load_dotenv
load_dotenv()
client = Together(api_key=os.getenv("TOGETHER_API_KEY"))
print("1. Generating an image for the scene...")
scene = " **Lily Finds the Grey Garden.** Once, a kind little girl named Lily discovered a secret garden behind an old, stone wall. But it was a sad garden! The flowers were droopy, the grass was grey, and even the sunshine seemed to avoid it. In the middle of the garden, she found a tiny, empty watering can with a note that read: "
response_img = client.images.generate(
        prompt=scene+" illustrated in colorful storybook / comic style, soft lighting, magical atmosphere, pastel colors, child-friendly.",
        model ="black-forest-labs/FLUX.1-schnell-Free",
        steps = 3,
        n=2,
        format="b64_json"
    )
print("2. Image generated successfully!")
print(response_img.data[0].b64_json)
