#!/usr/bin/python
# -*- coding:utf-8 -*-

import socket
import time


serverip = "192.168.43.131"
#client可变，谁是client，就要换成谁的ip
client_ip1 = "192.168.43.131"
serverport = 12345


#传输字符时要发送的东西
def msg_send():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#建立和server的连接
    client.connect((serverip, serverport))

    # Send msg transmission flag
    client.send("msg".encode("utf-8"))

    time.sleep(1)

    # IP send
    client.send(client_ip1.encode("utf-8"))

    print("Input massage:")

    msg = input()
    client.send(msg.encode("utf-8"))
    # print('Message: ', msg)
    print("")
    print("Sended")
    print("")
    client.close()


#传输文件时要发送的东西
def file_send():
    server = serverip

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#建立和server的连接
    client.connect((server, serverport))

    # Send file transmission flag
    client.send("file".encode("utf-8"))

    time.sleep(1)

    # Send IP
    client.send(client_ip1.encode("utf-8"))

    time.sleep(1)

    print("")
    file = input("Input  the path of the file:")
    path = input("Input the target location of the file:")

    client.send(path.encode("utf-8"))

    time.sleep(1)

#以二进制读文件到缓冲区
    file = open(file, "rb")

    while True:
        file_buffer = file.read(1024)
        if not file_buffer:
            break
        client.send(file_buffer)
#关闭连接

    client.close()

    print("\nsuccessful")



