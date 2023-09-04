from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import hashlib
import os
from .helper import AppHelper


def add_embedding(fileurl):
    #to-do : get unembedded files from blob storage
   loader = TextLoader(fileurl)
   docs = loader.load()

   text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 2000,
        chunk_overlap =0
   )
   split_docs  = text_splitter.split_documents(docs)

   keys = []
   
   for i, doc in enumerate(split_docs):
        hashKey = hashlib.sha1(f'{fileurl}_{i}'.encode("utf-8")).hexdigest()
        keys.append(hashKey)
        # doc.metadata ={"key":hashKey}
   store = AppHelper.store

   store.add_texts(texts = split_docs,keys = keys)

def get_all_embeddings():
     result = AppHelper.store.similarity_search(query="*")
     return list(map(lambda x: x["metadata"].key,result))

def delete_embedding(keys):
     docs = []
     for key in keys:
          docs.append({
               "@search.action":"delete",
               os.environ("AZURESEARCH_FIELDS_ID") :key
          })
     AppHelper.store.client.delete_documents(documents=docs)






