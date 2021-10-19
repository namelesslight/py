#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :thread.py
# @Time      :2021/10/16 14:52:39
# @Author    :ZCL

#该选项目编辑中
import _thread
import time

def print_time(threadName,delay):
    count=0
    while count<5:
        time.sleep(delay)
        count+=1
        print("{0}:{1}",(threadName,time.ctime(time.time())))
try:
    _thread.start_new_thread(print_time,("Thread-1",2,))
    _thread.start_new_thread(print_time,("Thread-2",4,))
except:
    print("Error")
while 1:
   pass