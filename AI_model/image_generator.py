import os
import requests
from together import Together
from dotenv import load_dotenv

load_dotenv()

def generate_image(prompt: str, index: int) -> str:
    """
    Generates an image using Together API,
    downloads it using the returned URL,
    saves as 'images/{index}.png', and returns the filepath.
    """
    client = Together(api_key=os.getenv("TOGETHER_API_KEY"))

    # Ensure 'images' folder exists
    output_dir = "images"
    os.makedirs(output_dir, exist_ok=True)

    # Generate image
    response = client.images.generate(
        prompt=prompt,
        model="black-forest-labs/FLUX.1-schnell-Free",
        steps=1,
        n=1,
        width=512,
        height=512,
        seed=None,
        format="url"  
    )

    image_url = response.data[0].url  
    image_data = requests.get(image_url).content

    filename = f"{index}.png"
    filepath = os.path.join(output_dir, filename)

    with open(filepath, "wb") as f:
        f.write(image_data)

    print(f"Image saved at: {filepath}")
    return filepath
