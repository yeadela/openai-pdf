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

def chat(request) :
    # init()
    # filePath="D:\\field-guide-to-data-science.pdf"
    # load = PyPDFLoader(filePath)
    # data = load.load()
    # text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=0)
    # texts = text_splitter.split_documents(data)
    # # loader=TextLoader(filePath)
    # documents = loader.load()
    # text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    # docs = text_splitter.split_documents(documents)
    embed = OpenAIEmbeddings(env.EMBEDDING_MODEL)
    #db = Pinecone.from_documents(docs, embed, index_name="adela")
    index_name = "adela"
    # if index_name not in pinecone.list_indexes():
    #     # we create a new index
    #     pinecone.create_index(
    #     name=index_name,
    #     metric='cosine',
    #     dimension=1536  
    #     )
    # The OpenAI embedding model `text-embedding-ada-002 uses 1536 dimensions`
    #db = Pinecone.from_documents(docs, embed, index_name=index_name)
    #db=Pinecone.from_existing_index(index_name, embed)
    #llm = OpenAI() #default model 
    #model_name='text-davinci-003',max_tokens=1500
    
    # qa = RetrievalQA.from_chain_type(llm, chain_type='map_rerank', retriever=db.as_retriever(),return_source_documents=True)
    # answer = qa({"query":"数学家兼信息论的祖师爷是谁"})
    # print(answer)
    #docsearch = Pinecone.from_texts([t.page_content for t in texts], embed, index_name=index_name)
    docsearch = Pinecone.from_existing_index(index_name=env.PINECONE_INDEX_NAME,embedding=embed)
   # llm = OpenAI(temperature=0)
    llm = ChatOpenAI(model_name = env.LLM_MODEL, temperature =0.0)
    chain = load_qa_chain(llm, chain_type="stuff")
    
    query = json.loads(request.body).get("prompt")
    #"What is the collect stage of data maturity?"
    docs = docsearch.similarity_search(query)
    answer=chain.run(input_documents=docs, question=query)
    print(answer)
    return JsonResponse({"answer":answer})