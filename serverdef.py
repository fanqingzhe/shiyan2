#!/usr/bin/python
# -*- coding:utf-8 -*-


#��Ϣ����
def msg_recv(server):
#�����Ϣ��Դip��ַ
    addr = server.recv(1024)
    print("Address:%s" % addr.decode('utf-8'))
#�����Ϣ����
    msg = server.recv(1024)
    print("  Message:%s" % msg.decode('utf-8'))
#�ر�����
    server.close()

#�����ļ�
def file_recv(server):
#��Դ��ip��ַ
    addr = server.recv(1024)
    print("Address:%s" % addr.decode('utf-8'))
#�ļ���������client���͵�����
    file_name = server.recv(1024).decode("utf-8")
  
#���ļ��Զ����ƶ���file��
    file=open(file_name,'wb')

    while True:
        data=server.recv(1024)
        if not data:
            break
#������յ������ݣ���д���ļ���
        file.write(data)
#�ر��ļ��Ա���
    file.close()
    print(" %s received" % file_name)



