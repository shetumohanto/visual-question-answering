import os
import base64
import requests
from io import BytesIO
from dotenv import load_dotenv
import anthropic

load_dotenv()

# Get OpenAI API Key from environment variable
api_key = os.environ["CLAUDE_API_KEY"]

client = anthropic.Anthropic(api_key=api_key)  

# Function to encode the image
def encode_image_from_file(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def encode_image_from_pil(image):
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode('utf-8')

def request_claude(system_message, user_message, image):
    image1_data = encode_image_from_pil(image)
    response = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1024,
        system = system_message, 
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/jpeg",
                            "data": image1_data,
                        },
                    },
                    {
                        "type": "text",
                        "text": "Describe this image."
                    }
                ],
            }
        ],
        )

    return response.content[0].text
