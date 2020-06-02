import socket
import matplotlib.pyplot as plt
import numpy as np

class tcpsercl():
    def client(self,address,port,filepath):
        c_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        c_addr=(address,port)
        c_socket.connect(c_addr)
        Flag=1
        count=0
        data=open('test.jpg','rb')
        c_socket.sendall(data)
        c_socket.close()
    
    def server(self,address,port):
        s_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s_address=(address,port)
        s_socket.bind(s_address)
        s_socket.listen(5)
        flag=1
        count=0
        while True:
            print(f'Listning at {address}:{port}')
            c_sock,c_addr=s_socket.accept()
            print(f'Got connection from {c_addr[0]}:{c_addr[1]}')
            data=c_sock.
            c_sock.sendall(data.encode())
        s_socket.close()

def server(medium):
    addr=input("Enter the server address :\n")
    medium.server(addr,5000)

def client(medium):
    addr=input("Enter the client address :\n")
    medium.client(addr,5000,"xxxxx")

if __name__=='__main__':
    alpha=int(input("Enter the choice :\n1.Server \n2.Client\n"))
    medium=tcpsercl()
    if alpha==1:
        server(medium)
    else:
        client(medium)