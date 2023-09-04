from .env import init
from langchain import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import Pinecone
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from django.http import JsonResponse
from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.question_answering import load_qa_chain
import json
from . import env
from .helper import AppHelper

def chat(request) :
    
    llm = ChatOpenAI(model_name = env.LLM_MODEL, temperature =0.0)
    chain = load_qa_chain(llm, chain_type="stuff")
    
    query = json.loads(request.body).get("prompt")
    #"What is the collect stage of data maturity?"
    docs = AppHelper.store.similarity_search(query)
    answer=chain.run(input_documents=docs, question=query)
    print(answer)
    return JsonResponse({"answer":answer})