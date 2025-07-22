from AI_model.prompt_templates import generate_image_prompt, generate_story_prompt
from AI_model.image_generator import generate_image
from AI_model.generate_story import generate_story 
from AI_model.extract_story_data import extract_story_data, extract_story_steps
import ast

if __name__ == "__main__":
    # Generate a story
    question = "detective duck named Ducky solves a mystery in a magical forest "
    story_response = generate_story(question)
    print("Story generated successfully!")

    story_response = extract_story_data(story_response)

    story_steps = extract_story_steps(str(story_response['story_steps']))
    story_steps = ast.literal_eval(story_steps[0])

    print(story_steps)
    urls = []
    for i in range(5):
        image_prompt = generate_image_prompt(
            setting=story_response['story_setting'],
            style=story_response['story_style'],
            character=story_response['main_character'],
            previous_scene=story_steps[i-1] if i > 0 else None,
            current_scene=story_steps[i]
        )

        generated_img = generate_image(image_prompt)
        urls.append(generated_img)

for i in range(5):
    print(f"Image {i+1} URL: {urls[i]}")