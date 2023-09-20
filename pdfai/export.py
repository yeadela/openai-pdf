import sqlite3  
import pandas as pd  
import matplotlib.pyplot as plt  
from matplotlib.backends.backend_pdf import PdfPages  
import shutil
import os
import json  
  
def query_to_excel(query, db_path, output_path):  
    # 连接到SQLite数据库  
    conn = sqlite3.connect(db_path)  
    cursor = conn.cursor()  
  
    # 执行查询  
    cursor.execute(query)  
  
    # 获取查询结果  
    results = cursor.fetchall()  
  
    # 将结果转换为DataFrame  
    df = pd.DataFrame(results, columns=[column[0] for column in cursor.description])  
  
    # 将DataFrame保存为Excel文件  
    df.to_excel(output_path, index=False)  
  
    # 关闭数据库连接  
    conn.close()  


def query_to_json(query):  
    # 连接到数据库  
    conn = sqlite3.connect('example.db')  
    conn.row_factory = sqlite3.Row  # 这将使你可以通过列名访问数据  
    cursor = conn.cursor()  
  
    # 执行查询  
    cursor.execute(query)  
  
    # 获取查询结果  
    results = cursor.fetchall()  
  
    # 将结果转换为字典列表，其中每个字典代表一行数据  
    data = [dict(row) for row in results]  
  
    # 将数据转换为JSON格式并返回  
    json_data = json.dumps(data)   
    return json_data


def data_to_pie(data,file_name,target_path):
      df = pd.DataFrame.from_dict(data, orient='index', columns=['value'])  
      fig, ax = plt.subplots() 
      ax.pie(df['value'], labels=df.index, autopct='%1.1f%%', startangle=90)  
      ax.axis('equal')
      plt.title('pie')  
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

def data_to_bar(data,file_name,target_path):
    df = pd.DataFrame(data)  
    plt.figure(figsize=(10,5)) 
    labels = list(data.keys()) 
    plt.plot(df[labels[0]], df[labels[1]], marker='o')  
    plt.title('Bar')  
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

