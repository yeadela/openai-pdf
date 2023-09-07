import os
import pinecone
from langchain.document_loaders import PyPDFLoader 
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
import tiktoken

#PINECONE_INDEX_NAME = "adela"
EMBEDDING_MODEL ="text-embedding-ada-002"
LLM_MODEL = 'gpt-3.5-turbo'

# tiktoken.encoding_for_model(LLM_MODEL)
# tokenizer = tiktoken.get_encoding("cl100k_base")

def init():
    print("---initiallizing start---")
    # init for openai(openai embedding, openai chat)
    os.environ["OPENAI_API_TYPE"] = "azure"
    os.environ["OPENAI_API_KEY"] ="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"
    #os.environ["OPENAI_API_BASE"] ="http://flag.smarttrot.com/index.php/api/v1" #https://<your-endpoint.openai.azure.com/
    # os.environ["OPENAI_API_VERSION"] = "2023-03-15-preview"

    #init for azure serach
    os.environ["AZURE_SEARCH_ENDPOINT"]="YOUR END POINT"
    os.environ["AZURE_SERACH_INDEX_NAME"]="YOUR INDEX NAME"
    os.environ["AZURE_SERACH_API_KEY"]="YOUR API KEY"
    os.environ["AZURESEARCH_FIELDS_ID"] ="id"

 

    # pinecone.init(
    #     api_key="ec70078b-04f8-4d91-8ebc-98ad36e923c1",
    #     environment="asia-southeast1-gcp-free"
    # )
    # init_index()
    
# def init_index():
#     if PINECONE_INDEX_NAME not in pinecone.list_indexes():
#         pinecone.create_index(name = PINECONE_INDEX_NAME,dimension = 1536,metric='cosine')
#     else:
#         filePath ="D:\\field-guide-to-data-science.pdf"
#         loader = PyPDFLoader(filePath)
#         docs = loader.load()
#         text_splitter = RecursiveCharacterTextSplitter(
#             chunk_size = 2000, 
#             chunk_overlap = 0,
#            # length_function = tiktoken_len
#            # separators= ["\n\n","\n"]
#         )
#         split_docs = text_splitter.split_documents(docs)

#         Pinecone.from_documents(split_docs,OpenAIEmbeddings(model = EMBEDDING_MODEL), index_name = PINECONE_INDEX_NAME)


# def tiktoken_len(text):  
#     tokens = tokenizer.encode(
#         text,
#         disallowed_special=()
#     )
#     return len(tokens)
    
