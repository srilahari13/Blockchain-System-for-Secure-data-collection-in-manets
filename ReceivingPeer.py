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
    #print(tmpData)
    a=tmpData[0]
    a=a.split(',')[0]
    b=tmpData[1]
    b=b.split(',')[0]
    c=tmpData[2]
    c=c[:-1]
    print(a,b,c)