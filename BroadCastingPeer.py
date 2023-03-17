import DataGeneration as DG
import time
import socket

ip='50.50.51.124'

def broadCastData(data):
    print(data)
    s=socket.socket()
    s.connect((ip,12345))
    s.send(data.encode('utf-8'))
    s.close()
    time.sleep(4)

while True:
    a,b,c=DG.getData()
    data='{"a": '+str(a)+', "b" :'+str(b)+', "c" :'+str(c)+'}'
    broadCastData(data)
    time.sleep(2)
