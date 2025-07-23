from AI_model.prompt_templates import generate_image_prompt, generate_story_prompt
from AI_model.image_generator import generate_image
from AI_model.generate_story import generate_story 
from AI_model.extract_story_data import extract_story_data, extract_story_steps, extract_visual_descriptions
from post_image_generation.add_text_layer import add_text_to_image

if __name__ == "__main__":
    # Step 1: Generate the story from question
    question = "A detective duck wearing a detective costume, solving a mystery of a 'egg' in a small town."
    raw_story = generate_story(question)
    print("Story generated successfully!")
    # Step 2: Extract structured information from the story
    story_response = extract_story_data(raw_story)
    story_steps = story_response["story_steps"]
    print(story_steps)
    # Step 3: Generate images using each visual description
    for i in range(5):
        image_prompt = generate_image_prompt(
            setting=story_response['story_setting'],
            style=story_response['story_style'],
            character=story_response['main_character'],
            visual_scene_description=story_steps[i]["visual_scene_description"],
        )
        print(i+1)
        generated_img_path = generate_image(image_prompt,i+1)
        add_text_to_image(generated_img_path, story_steps[i]["story_point"])

