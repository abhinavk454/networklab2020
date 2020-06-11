##########################
# Lab : Network Lab      #
# Name : Abhinav Kumar   #
# Enroll no.: 510817075  #
# Assignment : 04(Q.01)  #
##########################

# tcp client
import select
import socket
import sys


def Client(host='127.0.0.1', port=9002):
    s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_socket.connect((host, port))

    while True:
        sockets_list = [sys.stdin, s_socket]
        read_socket, write_socket, error_socket = select.select(
            sockets_list, [], [])
        for socks in read_socket:
            if socks == s_socket:
                message = socks.recv(2048)
                print(message.decode('ascii'))
            else:
                message = sys.stdin.readline()
                s_socket.send(message.encode())
                sys.stdout.write("You : ")
                sys.stdout.write(message)
                sys.stdout.flush()

    s_socket.close()


if __name__ == "__main__":
    print("Connecting to server on 127.0.0.1:9002 if server is at diff ip pass ip as argument in below function.\n")
    Client()
