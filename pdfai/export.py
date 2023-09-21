import pandas as pd  
import matplotlib.pyplot as plt  
from matplotlib.backends.backend_pdf import PdfPages  
import shutil
import os
import json  
from reportlab.pdfgen import canvas  
from reportlab.lib.pagesizes import letter  
from django.db import connection
from .uploadFile import mappingtransfer
from langchain.tools.azure_cognitive_services.form_recognizer import AzureCogsFormRecognizerTool
from azure.storage.blob import BlobServiceClient,BlobClient

from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
import os
from PIL import Image
  
def getDataFromDb(query=None, rule_id=None):  
    # 连接到SQLite数据库  
    # conn = sqlite3.connect(db_path)  
    cursor = connection.cursor()  
  
    # 执行查询  
    query = "select * from trades"
    cursor.execute(query)  
  
    # 获取查询结果  
    results = cursor.fetchall()  
  
    # 将结果转换为DataFrame  
    df = pd.DataFrame(results, columns=[column[0] for column in cursor.description])  
    rule_id = 9
    if rule_id != None:
        df = mappingtransfer(df,rule_id)
    # 将DataFrame保存为Excel文件  
    # df.to_excel(target_path, index=False)  
  
    # 关闭数据库连接  
    connection.close()  
    return df

def getDataFromExcel(file_name="data.xlsx"):
    file_path = os.path.dirname(os.path.abspath(__file__))
    base_path = os.path.join(file_path, file_name)
    return  pd.read_excel(base_path)

def getDataFromImages(file_name="test.pdf"):
    file_path = os.path.dirname(os.path.abspath(__file__))
    base_path = os.path.join(file_path, file_name)
    
    filename = "Trades.jpg"

    #store file to blob storage
    storage_account_url = f'https://{os.environ.get("STORAGE_ACCOUNT")}.blob.core.windows.net'
    
    storage_container = os.environ.get("STORAGE_CONTAINER")
   
    doc_analysis_client = DocumentAnalysisClient(
                    endpoint=os.environ.get("RECOGNIZER_ENDPOINT"),#"form recognizer endpoin",
                    credential=AzureKeyCredential(os.environ.get("RECOGNIZER_KEY")),
                )

    poller = doc_analysis_client.begin_analyze_document_from_url(
                "prebuilt-document", document_url = f'{storage_account_url}/{storage_container}/' + filename)
        

    result = poller.result()
    res_dict = [item.to_dict() for item in result.key_value_pairs]
    return pd.DataFrame.from_dict(res_dict)

def export_excel(df,target_path='share1.xlsx'):
    df.to_excel(target_path, index=False)  


def export_json(df):  
    df.to_json('data.json')


def data_to_pie(df,file_name,target_path = './mypy//'):
      df = df.from_dict(orient='index', columns=['value'])  
      fig, ax = plt.subplots() 
      ax.pie(df['value'], labels=df.index, autopct='%1.1f%%', startangle=90)  
      ax.axis('equal')
      plt.title('Pie')  
# 将饼图保存为PDF文件  
      pdf_pages = PdfPages(file_name)  
      pdf_pages.savefig(fig)  
      pdf_pages.close()

# 定义源文件和目标路径  
      source_file = './'+file_name  
#       target_path = 'E://AzureFolder//test'  
      file_name = os.path.basename(file_name)  # 获取源文件的文件名  
  
      target_file = os.path.join(target_path, file_name)  # 构建目标文件的完整路径  
      if os.path.exists(target_file):  
          os.remove(target_file)  # 删除目标文件 
  
# 使用shutil.move来移动文件  
      shutil.move(source_file, target_path)

def data_to_line(data,file_name,target_path= './mypy//'):
    df = pd.DataFrame(data)  
    plt.figure(figsize=(10,5)) 
    labels = list(data.keys()) 
    plt.plot(df[labels[0]], df[labels[1]], marker='o')  
    plt.title('Line')  
    labels = list(data.keys())
    plt.xlabel(labels[0])  
    plt.ylabel(labels[1])  
    
    # 把这个折线图保存为一个PDF文件  
    with PdfPages(file_name) as pdf:  
        pdf.savefig(plt.gcf())
    # 定义源文件和目标路径  
    source_file = './'+file_name  
#       target_path = 'E://AzureFolder//test'  
    file_name = os.path.basename(file_name)  # 获取源文件的文件名  

    target_file = os.path.join(target_path, file_name)  # 构建目标文件的完整路径  
    if os.path.exists(target_file):  
        os.remove(target_file)  # 删除目标文件 

# 使用shutil.move来移动文件  
    shutil.move(source_file, target_path)


def data_to_bar(data,file_name,target_path= './mypy//'):
    df = pd.DataFrame(data, index=['X', 'Y', 'Z'])
    c = canvas.Canvas(file_name, pagesize=letter)
    fig, ax = plt.subplots()  
    df.plot(kind='bar', ax=ax)  
    plt.savefig('bar_plot.png')  # 将图像保存到文件  
    c.drawImage('bar_plot.png', 50, 500, 600, 400)  # 将图像插入到PDF文件中  
    c.showPage()  
    c.save()   
    os.remove('./bar_plot.png')
    source_file = './'+file_name  
#       target_path = 'E://AzureFolder//test'  
    file_name = os.path.basename(file_name)  # 获取源文件的文件名  

    target_file = os.path.join(target_path, file_name)  # 构建目标文件的完整路径  
    if os.path.exists(target_file):  
        os.remove(target_file)  # 删除目标文件 

# 使用shutil.move来移动文件  
    shutil.move(source_file, target_path)


