from langchain.prompts import ChatPromptTemplate
import re

def generate_image_prompt(setting, style, character, current_scene, previous_scene=None):
    prompt = f"""
You are an image generation model helping illustrate a children's story.

Follow these global story settings, style guidelines, and main character references across all scenes for consistency.

---

**STORY SETTING**: {setting}  
This setting should stay visually consistent across all generated images, with coherent backgrounds, environments, and atmosphere.

**VISUAL STYLE**: {style}  
Keep the art style, textures, lighting, and color palette aligned with this description in every image you generate.

**MAIN CHARACTER**: {character}  
Ensure this character’s appearance (clothes, facial features, posture, emotions) remains consistent in each scene where they appear.
"""

    if previous_scene:
        prompt += f"""

---

**PREVIOUS SCENE CONTEXT**:  
{previous_scene}  

Carry over all visual and narrative elements (characters, items, mood, etc.) from this scene into the current one unless explicitly changed.
"""

    prompt += f"""

---

**CURRENT SCENE TO ILLUSTRATE**:  
{current_scene}  

This is one part of a continuous story.  
Ensure that:
- The style and setting match previous scenes
- The main character looks identical to earlier
- Objects, characters, and environment remain consistent
- Emotions and actions logically follow from the previous scene
"""

    return prompt


def generate_story_prompt():
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", """
You are a creative storyteller who writes magical short stories for children aged 5 to 10.

Your job is to create a fun, imaginative, and emotionally warm story that answers or relates to the question in a magical way.

Please follow this structure in your response:

---

**STORY SETTING:**  
Describe the overall setting or world where the story takes place. Keep it consistent across all steps.  
Example: “A floating candy island in the clouds where everything is made of desserts.”

**STORY STYLE:**  
Describe how the story would look if it were illustrated. Include art style, colors, lighting, mood, etc.  
Example: “Pastel-colored comic book style, soft lighting, glowing magical elements, child-friendly and dreamy.”

**MAIN CHARACTER:**  
Describe the main character of the story.  
Example: “A little 7-year-old girl named Lily with curly hair and a bright smile, wearing a yellow dress.”

---

**MAGICAL STORY IN 5 STEPS:**  
Write the story in 5 simple, numbered steps.  
Each step should be:
- One clear visual moment (for image generation)  
- Written in simple, joyful language suitable for children  
- Contain the main character, emotional tone, and visual elements

After each step, write:

 **Visual Scene Description**:  
Briefly describe the scene that should be shown in the image. Include:
- What’s happening  
- Who is present and where they are  
- Emotions and actions  
- Background, mood, lighting, and magical objects  

---

Start the story section with this header:  
**Here is your story in 5 magical steps:**
"""),
            ("human", "A child has asked to generate a story on the question: {question}")
        ]
    )
    return prompt
