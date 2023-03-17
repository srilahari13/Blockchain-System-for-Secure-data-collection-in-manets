import socket
import json
ip='50.50.51.124'
s=socket.socket()
s.bind((ip,12345))
s.listen(5)

while True:
    obj,addr=s.accept()
    print('Incoming Connection from BroadCast Peer',addr)
    tmpData=obj.recv(1024)
    # print(tmpData)
    tmpData=tmpData.decode('utf-8')
    tmpData=json.loads(tmpData)
    a=tmpData['a']
    b=tmpData['b']
    c=tmpData['c']
    print(a,b,c)