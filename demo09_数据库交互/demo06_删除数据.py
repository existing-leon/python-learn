import mysql.connector

try:
    # 建立数据库连接
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="my_test"
    )
    print("成功连接到数据库！")
    # 创建游标对象
    mycursor = mydb.cursor()

    # 删除
    sql = "delete from teacher where name = 'John';"
    mycursor.execute(sql)

    # 事务提交
    mydb.commit()

    print(mycursor.rowcount, "条记录被删除。")

    # 关闭游标和连接
    mycursor.close()
    mydb.close()
except mysql.connector.Error as err:
    print(f"连接数据库时出错: {err}")
