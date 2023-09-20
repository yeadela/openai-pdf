import pandas as pd  
import matplotlib.pyplot as plt  
from matplotlib.backends.backend_pdf import PdfPages 
import shutil
import os
# 用pandas创建一个简单的数据集  
'''
data = {'Year': [2016, 2017, 2018, 2019, 2020],  
        'Sales': [15000, 17000, 14500, 16000, 18000]}  
df = pd.DataFrame(data)  
  
# 用matplotlib创建折线图  
plt.figure(figsize=(10,5))  
plt.plot(df['Year'], df['Sales'], marker='o')  
plt.title('Bar')  
labels = list(data.keys())
plt.xlabel(labels[0])  
plt.ylabel(labels[1])  
  
# 把这个折线图保存为一个PDF文件  
with PdfPages('sales_over_years.pdf') as pdf:  
    pdf.savefig(plt.gcf())
'''
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

data = {'Year': [20160, 20170, 20180, 20190, 20200],  
        'Sales': [15000, 17000, 14500, 16000, 18000]}      
file_name = 'bar2.pdf'
path = 'E://AzureFolder//test'
data_to_bar(data, file_name, path)