#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :py_socket.py
# @Time      :2021/10/13 09:40:00
# @Author    :ZCL
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=9999
s.bind(('127.0.0.1',9999))
s.listen(10)
while True:
    clientsocket,addr=s.accept()
    print(str(addr))
    msg='欢迎访问W3Cschool教程！'+ "\r\n"
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()