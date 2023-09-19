import os
from langchain import OpenAI, SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from .utils import getReqParamValue
from .baseResponse import BaseResponse
from django.http import JsonResponse

def parseLLMRequest(request):
    db = SQLDatabase.from_uri(os.environ.get("DB_CONNECT_STR"))
    llm = OpenAI(temperature=0)
    db_chain = SQLDatabaseChain(llm=llm, database=db, verbose=True)
    query = getReqParamValue(request,"prompt")
    answer = db_chain.run(query)
    print('----llm answer---',answer)
    return JsonResponse(BaseResponse(1,{"answer":answer}))