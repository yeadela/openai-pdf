import pymssql
 
# 连接参数
server = 'server_name'
database = 'database_name'
username = 'username'
password = 'password'
 
# 建立连接
conn = pymssql.connect(server=server, database=database, user=username, password=password)
 
# 创建游标对象
cursor = conn.cursor()
 
# 执行SQL查询
cursor.execute("SELECT * FROM your_table")
 
# 获取查询结果
result = cursor.fetchall()
 
# 遍历结果
for row in result:
    print(row)
 
# 插入数据
insert_query = "INSERT INTO your_table (column1, column2) VALUES (%s, %s)"
insert_data = ('value1', 'value2')
cursor.execute(insert_query, insert_data)
 
# 更新数据
update_query = "UPDATE your_table SET column1 = %s WHERE id = %s"
update_data = ('new_value', 1)
cursor.execute(update_query, update_data) #参数化查询
 
# 删除数据
delete_query = "DELETE FROM your_table WHERE id = %s"
delete_data = (1,)
cursor.execute(delete_query, delete_data)
 
# 提交事务
conn.commit()
 
# 关闭游标
cursor.close()
