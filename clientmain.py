#!/usr/bin/python
# -*- coding:utf-8 -*-

import clientdef



#����ѡ�������Ϣ�����ļ����˳�
while True:
    choice = 0
    print("1:send message")
    print("2:send file")
    print("0:exit")
    choice = input("Input your choice:")
    if choice in['0', '1', '2']:
        if choice == '1':
            clientdef.msg_send()

        if choice == '2':
            clientdef.file_send()

        if choice == '0':
            break




