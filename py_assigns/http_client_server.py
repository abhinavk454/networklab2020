import socket
import matplotlib.pyplot as plt
import numpy as np

class assign2_q1():
    def client(self,address,port):
        clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        clientsocket.connect((address,port))
        message="GET http://127.0.0.1/alpha.txt HTTP/1.0\r\n\r\n".encode()
        clientsocket.send(message)
        while True:
            data=clientsocket.recv(512)
            if len(data)<1:
                break
            print(data.decode(),end=' ')
        clientsocket.close()

    def server(self,addr,port):
        serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            serversocket.bind((addr,port))
            serversocket.listen(5)
            while(1):
                clientsocket,clientaddr=serversocket.accept()
                data1=clientsocket.recv(5000).decode()
                data1=data1.split("\n")
                if(len(data1)>0):
                    print(data1[0])
                data="HTTP/1.1 200 OK\r\n"
                data+="Content-Type: text/html; charset=utf-8\r\n"
                data+="\r\n"
                data+="<html><body>HELOOOOOOOOOOO</body></html>\r\n"
                clientsocket.sendall(data.encode())
                clientsocket.shutdown(socket.SHUT_WR)
        except KeyboardInterrupt:
            print("Shutting down server ....")
        except Exception as e:
            print("Error......")
            print(e)
        serversocket.close()

def server(connection):
    connection.server(address,9000)

def client(connection):
    connection.client(address,9000)

if __name__=="__main__":
    connection=assign2_q1()
    choice=int(input("Press 1 for server and 2 for client.\n"))
    if choice==1:
        address=input("Enter the address to host server :\n")
        server(connection)
    elif choice==2:
        address=input("Enter the address of server to connect :\n")
        client(connection)
