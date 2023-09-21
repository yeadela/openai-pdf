import matplotlib.pyplot as plt  
from reportlab.pdfgen import canvas  
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages  
import shutil
import os
''' 
# 创建饼图  
data = {'category': ['A', 'B', 'C', 'D'],  
        'value': [4, 8, 12, 16]}  
df = pd.DataFrame.from_dict(data, orient='index', columns=['value'])  
# df = pd.DataFrame(data)  
fig, ax = plt.subplots()  
plt.title('pie')
ax.pie(df['value'], labels=df['category'], autopct='%1.1f%%')  
ax.axis('equal')  


# 将饼图保存为PDF文件  
pdf_pages = PdfPages('pieABCD1.pdf')  
pdf_pages.savefig(fig)  
pdf_pages.close()

# 定义源文件和目标路径  
source_file = './pieABCD1.pdf'  
target_path = 'E://AzureFolder//test'  
  
# 使用shutil.move来移动文件  
shutil.move(source_file, target_path)'''

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

#demo
data = {'A': 15, 'B': 30, 'C': 45, 'D': 10} 
file_name = 'pieABCD1.pdf'
path = 'E://AzureFolder//test'
data_to_pie(data, file_name,path)