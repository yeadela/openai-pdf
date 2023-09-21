from reportlab.pdfgen import canvas  
from reportlab.lib.pagesizes import letter  
import matplotlib.pyplot as plt  
import pandas as pd
import os
import shutil
'''  
# 创建数据  
data = {'A': [25, 34, 32], 'B': [20, 31, 29], 'C': [18, 33, 27]}  
df = pd.DataFrame(data, index=['X', 'Y', 'Z'])  
  
# 创建PDF文件并绘制条形图  
c = canvas.Canvas("output.pdf", pagesize=letter)  
fig, ax = plt.subplots()  
df.plot(kind='bar', ax=ax)  
plt.savefig('bar_plot.png')  # 将图像保存到文件  
c.drawImage('bar_plot.png', 50, 500, 600, 400)  # 将图像插入到PDF文件中  
c.showPage()  
c.save()
'''

def data_to_bar(data,file_name,target_path):
    df = pd.DataFrame(data, index=['X', 'Y', 'Z'])
    c = canvas.Canvas(file_name, pagesize=letter)
    fig, ax = plt.subplots()  
    df.plot(kind='bar', ax=ax)  
    plt.savefig('bar_plot.png')  # 将图像保存到文件  
    c.drawImage('bar_plot.png', 50, 500, 600, 400)  # 将图像插入到PDF文件中  
    c.showPage()
    os.remove('./bar_plot.png')  
    c.save()   

    source_file = './'+file_name  
#       target_path = 'E://AzureFolder//test'  
    file_name = os.path.basename(file_name)  # 获取源文件的文件名  

    target_file = os.path.join(target_path, file_name)  # 构建目标文件的完整路径  
    if os.path.exists(target_file):  
        os.remove(target_file)  # 删除目标文件 

# 使用shutil.move来移动文件  
    shutil.move(source_file, target_path)

data = {'A': [25, 34, 32], 'B': [20, 31, 29], 'C': [18, 33, 27]}  
file_name = 'line.pdf'
path = 'E://AzureFolder//test'
data_to_bar(data, file_name, path)