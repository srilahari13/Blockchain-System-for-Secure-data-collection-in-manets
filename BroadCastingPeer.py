import DataGeneration as DG
import time
import socket

ip=''

def broadCastData(data):
    print(data)
    s=socket.socket()
    s.connect(ip,12345)
    s.send(data)
    s.close()
    time.sleep(4)

while True:
    a,b,c=DG.getData()
    data={}
    data['a']=a;
    data['b']=b;
    data['c']=c;
    broadCastData(str(data))
    time.sleep(2)
