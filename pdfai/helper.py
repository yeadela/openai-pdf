from langchain.vectorstores import AzureSearch
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
import os

class AppHelper():
   store = AzureSearch(
        azure_search_endpoint=os.environ.get("AZURE_SEARCH_ENDPOINT"),
        azure_search_endpoint=os.environ.get("AZURE_SEARCH_API_KEY"),
        index_name=os.environ.get("AZURE_SEARCH_INDEX_NAME"),
        embedding_function=OpenAIEmbeddings().embed_query
   ) 

   
