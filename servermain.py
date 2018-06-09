#!/usr/bin/python
# -*- coding:utf-8 -*-

#����һ���׽��֣�˵��serverdef�������߳�
import socket
import serverdef
import threading

#��������IP��ַ���˿����Զ����
serverip = "192.168.43.131"
serverport = 12345


#����һ��server�׽��֣����ݱ��׽��֣�SOCK_DGRAM����TCP���������
server =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#�󶨶˿�
server.bind((serverip,serverport))
#������һ����5���ȴ��ͻ�����
server.listen(5)
#����Լ���IP��ַ
print("your ip",serverip)
#����msg���ַ��͵�
msg = ""

while True:
	#�����ͻ��˵�����
    client, addr = server.accept()

	#flag�������̣߳���flag�ж�
    flag = client.recv(1024)
	#��utf-8�ı��뷽ʽ����
    print(flag.decode("utf-8"))
#�ļ������̣߳�flag��client���͹�����
    if flag.decode("utf-8") == "file":
        dispose = threading.Thread(target=serverdef.file_recv, args=(client,))
        dispose.start()
#elif��else if���ַ������߳�
    elif flag.decode("utf-8") == "msg":
        dispose = threading.Thread(target=serverdef.msg_recv, args=(client,))
        dispose.start()


server.close()