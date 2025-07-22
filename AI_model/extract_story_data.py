import re
import json

def extract_story_data(llm_output: str) -> dict:
    """Returns a structured dictionary from the LLM output. refer story_dict for the structure."""
    # Use regular expressions to split and extract the structured sections
    setting_match = re.search(r"\*\*STORY SETTING:\*\*\n(.*?)\n\n", llm_output, re.DOTALL)
    style_match = re.search(r"\*\*STORY STYLE:\*\*\n(.*?)\n\n", llm_output, re.DOTALL)
    character_match = re.search(r"\*\*MAIN CHARACTER:\*\*\n(.*?)\n\n", llm_output, re.DOTALL)
    steps_match = re.search(r"\*\*Here is your story in 5 magical steps:\*\*\n\n(.*)", llm_output, re.DOTALL)

    # Extract and clean the story steps
    story_steps = []
    if steps_match:
        step_lines = steps_match.group(1).strip().split("\n")
        for line in step_lines:
            # Match lines like "1. This is step text"
            step_text = re.match(r"\d+\.\s+(.*)", line)
            if step_text:
                story_steps.append(step_text.group(1).strip())

    story_dict = {
        "story_setting": setting_match.group(1).strip() if setting_match else "",
        "story_style": style_match.group(1).strip() if style_match else "",
        "main_character": character_match.group(1).strip() if character_match else "",
        "story_steps": story_steps
    }

    return story_dict


def extract_story_steps(story_text: str) -> list:
    # Use regex to split on numbered bullet points (1. 2. 3...)
    steps = re.split(r"\n\d+\.\s+", story_text.strip())
    
    # Remove any empty strings and header
    steps = [step.strip() for step in steps if step and not step.startswith("Here is your story")]
    
    return steps

