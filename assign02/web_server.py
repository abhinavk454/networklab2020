##########################
# Lab : Network Lab      #
# Name : Abhinav Kumar   #
# Enroll no.: 510817075  #
# Assignment : 02(Q.01)  #
##########################


import socket


def web_server(host=socket.gethostname(), port=9002):
    # started a tcp socketendpoint
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind((host, port))  # allocate address to server
        server_socket.listen(1)  # listen for 1 request
        print(f"started server at http://{host}:{port} open url in browser")
        while True:
            clientsocket, clientaddr = server_socket.accept()
            data1 = clientsocket.recv(5000).decode()
            data1 = data1.split("\n")
            if(len(data1) > 0):
                print(data1[0])
            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            f = open('test.html')#host this file on server
            m = f.read()
            data += m
            clientsocket.sendall(data.encode())
            # closing client connection
            clientsocket.shutdown(socket.SHUT_WR)
    except KeyboardInterrupt:
        print("\nClosing server...")


if __name__ == "__main__":
    # if i want to start server on certain address and port
    # then i have to pass address and port as argument by default it's set to loopback addr
    web_server(host='127.0.0.1')

# i have used fstring in this assignment if during execution of this code error happens
# then python3 on your system needs upgrade means it's below 3.6
