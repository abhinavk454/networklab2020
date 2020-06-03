##########################
# Lab : Network Lab      #
# Name : Abhinav Kumar   #
# Enroll no.: 510817075  #
# Assignment : 02(Q.02)  #
##########################


import socket
import time


# created udp client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def udp_ping_client(host=socket.gethostname(), port=9002):
    # if we can't get response in certain time means packet was lost so created timeout
    client_socket.settimeout(3)
    # to collect total time in 10 request
    rtt = 0
    # no of successful ping in 10 request
    successful_ping = 0
    try:
        for i in range(1, 11):
            sending_time = time.time()
            try:
                # sending ping request to server
                client_socket.sendto('ping'.encode('ascii'), (host, port))
                print(f"sent ping:{i} at {time.ctime(sending_time)}")
                # got response from server
                data, server_address = client_socket.recvfrom(4096)
                print(f"got {data.decode('ascii')}")
                successful_ping += 1
                reciveing_time = time.time()
                rtt += reciveing_time-sending_time
            except socket.timeout:
                print("Packet lost.")
    finally:
        print(f"The average RTT for 10 ping is {rtt/successful_ping}s.")
        client_socket.close()


if __name__ == "__main__":
    # by default it will connect to host on 127.0.0.1
    # input argument needs to be given if want to connect certain host and port
    udp_ping_client()


# i have used fstring in this assignment if during execution of this code error happens
# then python3 on your system needs upgrade means it's below 3.6
