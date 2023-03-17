import socket

ip=''
s=socket.socket()
s.bind(ip,12345)
s.listen(5)

while True:
    obj,addr=s.accept()
    print('Incoming Connection from BroadCast Peer',addr)
    tmpData=s.recv(1024)
    print(tmpData)