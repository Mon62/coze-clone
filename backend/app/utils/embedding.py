import os
import openai
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import OnlinePDFLoader
from dotenv import load_dotenv, find_dotenv
from .exceptions import BAD_REQUEST


# Custom function to insert documents into Supabase with file_id
def insert_documents_with_file_id(docs, embeddings, supabase, table_name, file_id, knowledge_id):
    for doc in docs:
        try:
            embedding = embeddings.embed_query(doc.page_content)
            doc_metadata = doc.metadata 
            response = supabase.table(table_name).insert({
                #'id': str(doc.id),
                'file_id': file_id,
                'knowledge_id':knowledge_id,
                'content': doc.page_content,
                'metadata': doc_metadata,
                'embedding': embedding
            }).execute()
        except:
            raise BAD_REQUEST

def embedding_file_gpt(supabase,file_path,file_id,knowledge_id):
    _ = load_dotenv(find_dotenv())


    openai.api_key = os.environ['OPENAI_API_KEY']

    loader = OnlinePDFLoader(file_path = file_path)
    documents = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = text_splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()
    insert_documents_with_file_id(docs, embeddings, supabase, "documents", file_id,knowledge_id)
    return {"detail": "successfully embbedding"}



def get_document(supabase,knowledge_id,query_text):
    embeddings = OpenAIEmbeddings()
    query_embedding = embeddings.embed_query(query_text)
    try:
        response = supabase.rpc('match_documents', {
            'query_embedding': query_embedding,
            'input_knowledge_id': knowledge_id
        }).execute()
        return response.data
    except:
        raise BAD_REQUEST
    