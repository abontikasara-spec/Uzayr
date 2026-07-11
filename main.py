import base64, io, json
from io import BytesIO
import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from groq import Groq
import config

st.set_page_config(page_title="The AI X-Ray Vision", page_icon="🧪", layout="centered")

client = Groq(api_key=config.GROQ_API_KEY)
st.session_state.setdefault("xray_outputs", [])

PROMPT = """Analyze this image and return ONLY valid JSON.
Identify all clearly visible important objects in the image.
For each object, return: name, short_label, fun_metadata, confidence, box
The "box" must use percentages 0 to 100 with x, y, w, h.
Rules:
- Include all clearly visible important objects
- Do not guess hidden or unclear objects
- If unsure, skip the object
- Keep labels short and kid-friendly
- Confidence must be one of: high, medium, low
- Never identify a real person by name
- If a person appears, use generic labels like "person", "smiling adult", "child", or "seated person"
- Do not guess identity, age, profession, or relationship
- Return JSON only
Format:
{"scene_title":"short futuristic title","objects":[{"name":"person","short_label":"smiling adult","fun_metadata":"person detected near the center","confidence":"high","box":{"x":20,"y":10,"w":25,"h":60}}]}"""

PERSON_WORDS = {"person", "adult", "child", "woman", "man", "girl", "boy", "human", "people"}
SAFE_LABELS = {"person", "smiling adult", "child", "seated person"}

st.title("🧪 The AI X-Ray Vision")
st.write("Upload a real photo and turn it into AI scanner images.")
st.markdown(
    "This app scans your image, finds important objects, "
    "and creates clean scanner-style images in smaller groups."
)

# -------------------------------
# Next Steps:
# 1. Add page title, description, and instructions
# 2. Create helper function to analyze the uploaded image with Groq Vision
# 3. Create helper function to convert percentage boxes into pixel coordinates
# 4. Create helper function to clean, filter, and prepare detected objects
# 5. Create helper function to split objects into groups
# 6. Create helper function to load fonts and draw the scanner HUD overlay
# 7. Create helper function to convert final image into downloadable bytes
# 8. Add file uploader and group-size selector
# 9. Preview the uploaded image
# 10. Add button to scan the image and generate grouped scanner outputs
# 11. Display all generated scanner images
# 12. Add download button for each scanner image
# -------------------------------