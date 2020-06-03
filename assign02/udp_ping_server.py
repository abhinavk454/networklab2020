##########################
# Lab : Network Lab      #
# Name : Abhinav Kumar   #
# Enroll no.: 510817075  #
# Assignment : 02(Q.02)  #
##########################


import socket
import random
import time
# server endpoint with udp
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def udp_ping_server(host=socket.gethostname(), port=9002):
    try:
        server_socket.bind((host, port))  # binding server with address
        print(
            f"started udp server on {host}:{port} at {time.ctime(time.time())}")
        while True:
            # to generate situation like packet loss that occurs in udp
            rand = random.randint(0, 100)
            # recives request
            message, client_address = server_socket.recvfrom(1024)
            print(
                f"got {message.decode('ascii')} from {client_address[0]}:{client_address[1]}")
            # probability of packet loss is low
            if rand < 3:
                continue
            # send response to client
            server_socket.sendto('pong'.encode('ascii'), client_address)
    except KeyboardInterrupt:
        print("\nClosing server...")


if __name__ == "__main__":
    # by default it will host on 9002 port and 127.0.0.1
    # input argument needs to be given to host on certain host and port
    udp_ping_server()
