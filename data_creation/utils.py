
import sys
import os

import base64
import requests
import random
from openai import OpenAI
import sys

OPENAI_KEY = "YOUR API KEY"
client = OpenAI(
    api_key=OPENAI_KEY,  
    base_url=''
)


def llm_generate(prompt, max_tokens=500, temperature=0.1):
    
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini-2024-07-18",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.1
        )
        response = completion.choices[0].message.content
        
    except Exception as e:
        print("Error during OpenAI API call:", e)
        response = ""
            
    return response