from .env import init
from langchain import OpenAI
from langchain.chains.summarize import load_summarize_chain

from langchain.document_loaders import PyPDFLoader
from django.http import JsonResponse
from langchain.text_splitter import RecursiveCharacterTextSplitter
def summarize(request) :
    init()
    filePath="D:\\field-guide-to-data-science.pdf"
    load = PyPDFLoader(filePath)
    # docs = load.load_and_split()
    data = load.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=0)
    texts = text_splitter.split_documents(data)

    llm = OpenAI(model_name="gpt-3.5-turbo") #default model 
    #model_name='text-davinci-003',max_tokens=1500

    chain = load_summarize_chain(llm, chain_type='refine', verbose=True)

    summ=chain.run(texts[:2])
    print(summ)
    return JsonResponse({"data":summ})
    