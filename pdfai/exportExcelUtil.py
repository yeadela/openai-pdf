import sqlite3  
import pandas as pd  
  
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
  
# demo  
query = "SELECT shares FROM Trades"  
db_path = "example.db"  
output_path = "shares2.xlsx"  
query_to_excel(query, db_path, output_path)