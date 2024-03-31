import pandas as pd
import pyodbc

# 加载更新后的 CSV 文件
updated_csv_file = r".\GeoMap.csv"
updated_data = pd.read_csv(updated_csv_file)

# 连接到 SQL Server 数据库
conn = pyodbc.connect('DRIVER={SQL Server};'
                      'SERVER=10.110.190.203\SQL2017EXPR;'
                      'DATABASE=TAIPowerGeology;'
                      'UID=ge_taipower;'
                      'PWD=1qazXSW@')

# 提取 SQL Server 数据表的数据
sql_query = "SELECT * FROM [TAI_GeoMap]"
sql_data = pd.read_sql(sql_query, conn)

# 比较数据
# 假设你的数据有一个唯一的标识列，比如 'ID' 列
# 将 SQL Server 数据表中不存在于 CSV 文件中的行提取出来
missing_from_sql = updated_data[~updated_data['FileName'].isin(sql_data['FileName'])]

# 将 SQL Server 数据表中存在但 CSV 文件中不存在的行提取出来
#missing_from_csv = sql_data[~sql_data['ID'].isin(updated_data['ID'])]

# 执行更新操作
cursor = conn.cursor()

try:
    # 将 CSV 文件中不存在于 SQL Server 数据表中的行插入到数据表中
    for index, row in missing_from_sql.iterrows():
        cursor.execute("INSERT INTO [TAI_GeoMap] (SerialNumber, FileName, FigureName) VALUES (?, ?, ?)", 
                       row['SerialNumber'], row['FileName'], row['FigureName'])

    # 将 SQL Server 数据表中存在但 CSV 文件中不存在的行删除
    # for index, row in missing_from_csv.iterrows():
    #     cursor.execute("DELETE FROM YourTable WHERE ID = ?", row['ID'])

    # 提交事务
    conn.commit()
    print("更新成功！")
except Exception as e:
    # 如果更新操作失败，回滚事务
    conn.rollback()
    print("更新失败:", e)
finally:
    # 关闭游标和连接
    cursor.close()
    conn.close()
