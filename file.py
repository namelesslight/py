#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :file.py
# @Time      :2021/10/18 09:20:22
# @Author    :ZCL
import pickle
#读取文件
f1=open('a.txt','a',encoding='utf-8')
f1.write('写入内容1')
f1.close()

#不存在则创建一个文件
f2=open('b.txt','a',encoding='utf-8')
f2.write('写入内容2')
f2.close()

#读取文件第二个参数的设置
# r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
# w	打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
# wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# r+	打开一个文件用于读写。文件指针将会放在文件的开头。
# w+	打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
# rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
# wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。