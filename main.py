import io
import streamlit as st
from huggingface_hub import InferenceClient
import config

st.set_page_config(page_title="AI Avatar Creator", page_icon="🎨", layout="centered")

OPTIONS = {
    "avatar type": ["boy hero", "girl hero", "wizard", "robot explorer", "space warrior", "animal adventurer"],
    "hairstyle": ["short spiky hair", "curly hair", "long straight hair", "ponytail", "glowing hair", "helmet"],
    "outfit": ["superhero suit", "magical robe", "space armor", "casual hoodie", "battle costume", "royal outfit"],
    "expression": ["happy", "confident", "excited", "brave", "mysterious", "playful"],
    "background": ["forest", "space station", "magic castle", "city skyline", "rainbow world", "cloud kingdom"],
    "art style": ["cartoon style", "anime style", "3D game style", "fantasy illustration", "comic style"],
}

client = InferenceClient(api_key=config.HF_API_KEY)
st.session_state.setdefault("generated_image", None)

# -------------------------------
# Next Steps:
# 1. Add UI elements (title, description, and instructions)
# 2. Create prompt mode selection (Avatar Builder / Custom Prompt)
# 3. Build avatar input fields using OPTIONS
# 4. Generate final prompt based on user input
# 5. Show prompt preview (optional)
# 6. Add button to generate avatar using Hugging Face model
# 7. Display generated image
# 8. Add download button for the image
# -------------------------------