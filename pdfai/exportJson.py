import sqlite3  
import json  
  
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
  
# 使用示例  
query = "SELECT shares FROM Trades"  
json_result = query_to_json(query)  
with open('shares.json', 'w') as f:  
    json.dump(json_result, f) 
print(json_result)