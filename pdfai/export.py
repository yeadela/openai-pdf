import pandas as pd  
import matplotlib.pyplot as plt  
from matplotlib.backends.backend_pdf import PdfPages  
import shutil
import os
import json  
from reportlab.pdfgen import canvas  
from reportlab.lib.pagesizes import letter  
from django.db import connection
  
def getDataFromDb(query=None):  
    cursor = connection.cursor()  
   
    query = "select * from trades"
    cursor.execute(query)  
    
    results = cursor.fetchall()  
  
    df = pd.DataFrame(results, columns=[column[0] for column in cursor.description])  
  
    connection.close()  
    return df


def export_excel(df,target_path='share.xlsx'):
    df.to_excel(target_path, index=False)  


def export_json(df):  
    df.to_json('data.json')


def data_to_pie(df,file_name,target_path = './mypy//'):
      df = df.from_dict(orient='index', columns=['value'])  
      fig, ax = plt.subplots() 
      ax.pie(df['value'], labels=df.index, autopct='%1.1f%%', startangle=90)  
      ax.axis('equal')
      plt.title('Pie')  
      pdf_pages = PdfPages(file_name)  
      pdf_pages.savefig(fig)  
      pdf_pages.close()
 
      source_file = './'+file_name  
      file_name = os.path.basename(file_name) 
  
      target_file = os.path.join(target_path, file_name) 
      if os.path.exists(target_file):  
          os.remove(target_file)   
  
      shutil.move(source_file, target_path)

def data_to_line(df,file_name,target_path= './mypy//'):
    # df = pd.DataFrame(data)  
    plt.figure(figsize=(10,5)) 
    # labels = list(data.keys()) 
    plt.plot(df['Year'], df['Sales'], marker='o')  
    plt.title('Line')  
    # labels = list(data.keys())
    plt.xlabel('Year')  
    plt.ylabel('Sales')  
     
    with PdfPages(file_name) as pdf:  
        pdf.savefig(plt.gcf())

    source_file = './'+file_name   
    file_name = os.path.basename(file_name)  

    target_file = os.path.join(target_path, file_name)
    if os.path.exists(target_file):  
        os.remove(target_file)   
 
    shutil.move(source_file, target_path)


def data_to_bar(df,file_name,target_path= './mypy//'):
    # df = pd.DataFrame(data, index=['X', 'Y', 'Z'])
    c = canvas.Canvas(file_name, pagesize=letter)
    fig, ax = plt.subplots()  
    df.plot(kind='bar', ax=ax)  
    plt.savefig('bar_plot.png')  
    c.drawImage('bar_plot.png', 50, 500, 600, 400) 
    c.showPage()  
    c.save()   
    os.remove('./bar_plot.png')
    source_file = './'+file_name  
    file_name = os.path.basename(file_name)  

    target_file = os.path.join(target_path, file_name)  
    if os.path.exists(target_file):  
        os.remove(target_file) 
  
    shutil.move(source_file, target_path)


