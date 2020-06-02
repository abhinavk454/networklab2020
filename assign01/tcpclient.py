##########################
# Lab : Network Lab      #
# Name : Abhinav Kumar   #
# Enroll no.: 510817075  #
# Assignment : 01(Q.01)  #
##########################
import socket


def tcpclient(host=socket.gethostname(), port=9002):
    # created client endpoint
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))  # request connection from server
    message = client_socket.recv(1024).decode('ascii')  # gets response
    print(message)  # prints response to terminal
    client_socket.close()  # closed client endpoint


if __name__ == "__main__":
    # if i want to connect to remote tcp server then i have to
    # pass its ip and port as argument of function below by default it will connect to 127.0.0.1
    tcpclient()
