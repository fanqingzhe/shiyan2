#!/usr/bin/python
# -*- coding:utf-8 -*-

#定义一个套接字，说明serverdef，定义线程
import socket
import serverdef
import threading

#服务器的IP地址，端口是自定义的
serverip = "192.168.43.131"
serverport = 12345


#定义一个server套接字，数据报套接字（SOCK_DGRAM），TCP传输用这个
server =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定端口
server.bind((serverip,serverport))
#监听，一般是5，等待客户连接
server.listen(5)
#输出自己的IP地址
print("your ip",serverip)
#定义msg是字符型的
msg = ""

while True:
	#建立客户端的连接
    client, addr = server.accept()

	#flag：创建线程，用flag判断
    flag = client.recv(1024)
	#以utf-8的编码方式解码
    print(flag.decode("utf-8"))
#文件接收线程，flag是client发送过来的
    if flag.decode("utf-8") == "file":
        dispose = threading.Thread(target=serverdef.file_recv, args=(client,))
        dispose.start()
#elif是else if，字符接收线程
    elif flag.decode("utf-8") == "msg":
        dispose = threading.Thread(target=serverdef.msg_recv, args=(client,))
        dispose.start()


server.close()