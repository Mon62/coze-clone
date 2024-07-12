import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

google_api_key = os.environ['GOOGLE_API_KEY']
genai.configure(api_key=google_api_key) 

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  }
]

model = genai.GenerativeModel(model_name='gemini-pro', safety_settings=safety_settings)

def summarize(message_history) -> str:
    prompt_part = [
    f'''Bạn là hãy tóm tắt cuộc hội thoại sau giữa người và một chatbot AI:
    {message_history}
    Bản tóm tắt:
    '''
    ]
    respone = model.generate_content(prompt_part)
    return respone.text