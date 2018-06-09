#!/usr/bin/python
# -*- coding:utf-8 -*-


#消息接收
def msg_recv(server):
#输出消息来源ip地址
    addr = server.recv(1024)
    print("Address:%s" % addr.decode('utf-8'))
#输出消息内容
    msg = server.recv(1024)
    print("  Message:%s" % msg.decode('utf-8'))
#关闭连接
    server.close()

#接收文件
def file_recv(server):
#来源的ip地址
    addr = server.recv(1024)
    print("Address:%s" % addr.decode('utf-8'))
#文件名字来自client发送的内容
    file_name = server.recv(1024).decode("utf-8")
  
#把文件以二进制读到file里
    file=open(file_name,'wb')

    while True:
        data=server.recv(1024)
        if not data:
            break
#如果接收到了内容，就写到文件里
        file.write(data)
#关闭文件以保存
    file.close()
    print(" %s received" % file_name)



