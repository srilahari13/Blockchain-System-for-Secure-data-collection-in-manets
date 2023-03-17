import socket

ip='50.50.51.124'
s=socket.socket()
s.bind((ip,12345))
s.listen(5)

while True:
    obj,addr=s.accept()
    print('Incoming Connection from BroadCast Peer',addr)
    tmpData=obj.recv(1024)
    print(tmpData)