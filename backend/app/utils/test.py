import os
import openai
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import OnlinePDFLoader
from dotenv import load_dotenv, find_dotenv


file_path = "https://ocqssqkjzmnmxxfdtdzb.supabase.co/storage/v1/object/sign/file/33?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJmaWxlLzMzIiwiaWF0IjoxNzIxMTg1NzQwLCJleHAiOjE3MjExODkzNDB9.a7AGbkOvSB6UgEunzUzfyJiQvOvInpR2fgj_NLvnC-Y"

loader = OnlinePDFLoader(file_path = file_path)
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
docs = text_splitter.split_documents(documents)
print(docs[7])