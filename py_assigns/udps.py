import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
address=('127.0.0.1',2000)
s.bind(address)
print(f'Listening at {address}')
while True:
    data,caddr=s.recvfrom(1024)
    msg=data.decode('ascii')
    print("The clint {} want to say {!r}".format(caddr,msg))
    s.sendto(data,caddr)