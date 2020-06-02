##########################
# Lab : Network Lab      #
# Name : Abhinav Kumar   #
# Enroll no.: 510817075  #
# Assignment : 01(Q.01)  #
##########################
import socket


def tcpserver(host=socket.gethostname(), port=9002):
    # started a tcp socketendpoint
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))  # allocate address to server
    server_socket.listen(5)  # listen for request
    print(f"started server at : {host}:{port}")
    while True:
        client_socket, client_address = server_socket.accept()  # accepts requests
        print(f"got request from {client_address[0]}:{client_address[1]}")
        message = 'you will get this message if connection is successful'
        # decoding bytecoded message to readable
        client_socket.send(message.encode('ascii'))
        print(f"sent response to {client_address[0]}:{client_address[1]}")
        client_socket.close()  # closing client connection


if __name__ == "__main__":
    # if i want to start server on certain address and port
    # then i have to pass address and port as argument by default it's set to loopback addr
    tcpserver()

# i have used fstring in this assignment if during execution of this code error happens
# then python3 on your system needs upgrade means it's below 3.6
