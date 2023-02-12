from pymysql import Connection

conn = Connection(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="12345678",
    autocommit=False
)

print(conn.get_server_info())

cursor = conn.cursor()
conn.select_db("mybatis")
cursor.execute("SELECT * from consult_content")
result = cursor.fetchall()
for line in result:
    print(line)

# 执行更改语句时需要commit才生效
# conn.commit()

conn.close()
