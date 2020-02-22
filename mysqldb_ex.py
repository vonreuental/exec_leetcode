# -*- coding: UTF-8 -*-
# 导入pymysql模块
import pymysql

# 连接database
db = pymysql.connect(
    host="10.138.227.155",
    user="ups_test",
    password="uPs_teSt0423",  # 写上你的数据库密码
    database='ups_test',
    charset='utf8'
)


def db_version():
    # 获取操作游标
    cursor = db.cursor()
    # 执行 SQL 语句
    cursor.execute("SELECT VERSION()")
    # 获取一条数据
    data = cursor.fetchone()
    print("MySQL 版本: %s " % data)
    # 关闭游标 & 数据库连接
    cursor.close()
    db.close()


def search():  # 获取操作游标
    cursor = db.cursor()
    # 执行 SQL 语句
    cursor.execute('SELECT * FROM heros WHERE hp_max > 6000;')
    # 获取一条数据
    data = cursor.fetchall()
    for each_player in data:
        print(each_player)

    # 关闭游标 & 数据库连接
    cursor.close()
    db.close()


# db_version()
search()
