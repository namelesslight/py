#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :jdbc.py
# @Time      :2021/10/11 13:27:31
# @Author    :ZCL

import pymysql
db =pymysql.connect(host='localhost',port=3306,user='',passwd='',database='test')
c=db.cursor()
try:
    c.execute("""
    insert into user values(1,'zcl')
    insert into user values(2,'zhaochanglang')
    """)
    s=db.commit()
except:
    db.rollback()
    print("Error")
else:
    print(s)

try:
    c.execute("""select * from people""")
    data=c.fetchall()
except:
    print('Error')
else:
    print(data)

try:
    c.execute("""update people set values(3,'zcl') where name='zcl'""")
    s=db.commit()
except:
    db.rollback()
    print('Error')
else:
    print(s)


try:
    c.excute("""delete from people where name='zcl'""")
    s-db.commit()
except:
    db.rollback()
    print('Error')
else:
    print(s)
db.close()