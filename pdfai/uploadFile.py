import os
from azure.storage.blob import BlobServiceClient,BlobClient
import pandas as pd
from .rules import RuleMapping
from django.db import connection
from .baseResponse import BaseResponse
from django.http import JsonResponse
from django.db import transaction
from .models import Trades
from .handle import *

@transaction.atomic
def read_file(file,rule_id, table_name):
    # df = pd.read_excel(file)
    if file.name.endswith('xlsx'):
        df = pd.read_excel(file)
    elif file.name.endswith('csv'):
        df = pd.read_csv(file)
    df = df.fillna("null-tag")
    rm = RuleMapping.objects.filter(rule_id = rule_id)
   
    for index, row in df.iterrows(): 
            md = Trades() if table_name == None else Trades()
            for item in rm:
                if item.handler != None:
                    src_val = row.get(item.source_column) if row.get(item.source_column) !="null-tag" else None
                    dest_val = eval(item.handler)(src_val)
                print("---item---",row.get(item.source_column))
                setattr(md,item.dest_column, dest_val)
            md.save()

    return BaseResponse.success()

def uploadFiles(request):
    rule_id = request.POST["rule_id"]
    file = request.POST["file"]
    table_name = request.POST["table_name"]
     # #store file to blob storage
    storage_account_url = f'https://{os.environ.get("STORAGE_ACCOUNT")}.blob.core.windows.net'
    storage_container = os.environ.get("STORAGE_CONTAINER")
    blob_service_client = BlobServiceClient(account_url=storage_account_url,credential=os.environ.get("STORAGE_KEY"))
    blob_client = blob_service_client.get_blob_client(container=storage_container, blob=file.filename)
    blob_client.upload_blob(file)

    ref = f'{storage_account_url}/{storage_container}/' + file.filename
    file.seek(0,0)
    return read_file(file,rule_id, table_name)

    

def uploadFiles1(request):
    file_path = os.path.dirname(os.path.abspath(__file__))
    base_path = os.path.join(file_path, 'data.xlsx')
    # df = pd.read_excel(file) 
   
    return read_file(base_path, 1, 'trades')

