import base64
import requests
import random
from openai import OpenAI
import sys
import os
# from main import OPENAI_KEY
OPENAI_KEY = "YOUR_OPENAI_KEY"  # todo: set your openai key here

client = OpenAI(
    api_key=OPENAI_KEY,  
    base_url=''
)

def generate_lvlm(prompt, image_path, model="gpt-4o", max_tokens=1000, temperature=0.1):
    # Encode function
    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    # Getting the base64 string
    base64_image = encode_image(image_path)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_KEY}"
    }
   
    payload = {
        "model": f"{model}",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": max_tokens,
        "temperature": temperature
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    
    response_json = response.json()
    return response_json['choices'][0]['message']['content']

