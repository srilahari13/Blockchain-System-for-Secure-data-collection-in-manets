import socket

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
    tmpData=tmpData.split(': ')
    print(tmpData[3])
    a=tmpData[1][1:]
    b=tmpData[3][1:]
    c=tmpData[5][1:-2]
    print(a,b,c)