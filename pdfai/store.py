from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from django.http import JsonResponse
import hashlib
import os
from .helper import AppHelper
import re
from langchain.document_loaders import PyPDFLoader
# import fitz # 一个用于处理PDF、XPS和其他文档格式的库
# from PIL import Image


def add_embedding(fileurl):
    #to-do : get unembedded files from blob storage
   loader = TextLoader(fileurl)
   docs = loader.load()

   text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 2000,
        chunk_overlap =80
   )
   split_docs  = text_splitter.split_documents(docs)

   keys = []
   
   for i, doc in enumerate(split_docs):
        hashKey = hashlib.sha1(f'{fileurl}_{i}'.encode("utf-8")).hexdigest()
        keys.append(hashKey)
        # doc.metadata ={"key":hashKey}
   store = AppHelper.getStore()
   store.add_texts(texts = split_docs,keys = keys)
   return JsonResponse({"data:":"add successful."})

def get_all_embeddings():
     result = AppHelper.getStore().similarity_search(query="*")
     return list(map(lambda x: x["metadata"].key,result))

def delete_embedding(keys):
     docs = []
     for key in keys:
          docs.append({
               "@search.action":"delete",
               os.environ("AZURESEARCH_FIELDS_ID") :key
          })
     AppHelper.getStore().client.delete_documents(documents=docs)
     return JsonResponse({"data:":"delete successful."})

def extract_text_from_PDF(files):
    # 参考官网链接：https://python.langchain.com/docs/modules/data_connection/document_loaders/pdf
     text = ""
    # multiply PDF file
#     for pdf in files:
#         pdf_reader = PyPDfLoader(pdf)
#         for page in pdf_reader.pages:
#             text += page.extract_text()
     # single file
     pdf_reader = PyPDFLoader(files)
     for page in pdf_reader.pages:
          text += page.extract_text()
     return text

def process_file(self, file: str):
        # 加载PDF文档
        loader = PyPDFLoader(file.name)
        documents = loader.load()
        # 下面是正则匹配，用于找出文件名，pattern的作用：找到字符串末尾最后一个/之后的部分
        # 举例说明，假设文件路径: /home/user/documents/myfile.pdf，
        # 返回的match : /myfile.pdf ,
        # match.group() 返回/myfile.pdf， match.group(1) 返回 myfile.pdf
        pattern = r"/([^/]+)$"
        match = re.search(pattern, file.name)
        file_name = match.group(1)
        return documents, file_name

# def render_file(file):
#     # 打开PDF文档
#     doc = fitz.open(file.name)
#     # 根据页面获取当页的内容
#     page = doc[app.page_num]
#     # 将页面渲染为分辨率为300 DPI的PNG图像，从默认的72DPI转换到300DPI
#     picture = page.get_pixmap(matrix=fitz.Matrix(300/72, 300/72))
#     # 从渲染的像素数据创建一个Image对象
#     image = Image.frombytes("RGB", [picture.width, picture.height], picture.samples)
#     # 返回渲染后的图像
#     return image

# def render_first(file):
#     document = fitz.open(file)
#     page = document[0]
#     picture = page.get_pixmap(matrix=fitz.Matrix(300 / 72, 300 / 72))
#     image = Image.frombytes("RGB", [picture.width, picture.height], picture.samples)
#     return image, []




