import google.generativeai as genai
from langchain.chains.question_answering import load_qa_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.prompts import ChatPromptTemplate
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

import os
from dotenv import load_dotenv

load_dotenv()

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

google_api_key = os.environ.get('GOOGLE_API_KEY')
gemini_pro_api_key = os.environ.get('GEMINI_PRO_API_KEY')

genai.configure(api_key=google_api_key)

def gennerate_response(prompt, config) -> str:
    llm = ChatGoogleGenerativeAI(google_api_key=google_api_key,
                                temperature=config['temperature'], 
                                max_tokens=config['max_tokens'], 
                                top_p=config['top_p'], top_k=config['top_k'], 
                                model_name=config['model_name'], 
                                max_output_tokens=config['max_output_tokens'],
                                top_k=config['top_k'],
                                safety_settings=safety_settings)
    
    return llm.invoke(prompt)