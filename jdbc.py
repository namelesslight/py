#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :jdbc.py
# @Time      :2021/10/11 13:27:31
# @Author    :ZCL

import pymysql
db =pymysql.connect(host='localhost',port=3306,user='',passwd='',database='test')
#连接数据库
c=db.cursor()
#添加
try:
    c.execute("""
    insert into user values(1,'zcl')
    insert into user values(2,'zhaochanglang')
    """)
    #执行，返回执行成功行数
    s=db.commit()
except:
    #失败回滚
    db.rollback()
    print("Error")
else:
    print(s)
#查询
try:
    #设置sql语句
    c.execute("""select * from people""")
    #获取内容
    data=c.fetchall()
except:
    print('Error')
else:
    print(data)
#修改
try:
    #设置sql语句
    c.execute("""update people set values(3,'zcl') where name='zcl'""")
    #执行，返回执行成功行数
    s=db.commit()
except:
    #失败回滚
    db.rollback()
    print('Error')
else:
    print(s)
#删除
try:
    #设置sql语句
    c.excute("""delete from people where name='zcl'""")
    #执行，返回执行成功行数
    s=db.commit()
except:
    #失败回滚
    db.rollback()
    print('Error')
else:
    print(s)
db.close()