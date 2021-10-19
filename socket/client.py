#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :client.py
# @Time      :2021/10/14 09:01:12
# @Author    :ZCL
import socket
import sys

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=socket.gethostname()
port=9998
s.connect(('127.0.0.1',9999))
msg=s.recv(1024)
s.close()
print(msg.decode('utf-8'))