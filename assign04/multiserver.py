##########################
# Lab : Network Lab      #
# Name : Abhinav Kumar   #
# Enroll no.: 510817075  #
# Assignment : 04(Q.01)  #
##########################

# tcp server with threads to handle multi clients only text data transfer
import socket
import select
import _thread


def Server(host='127.0.0.1', port=9002):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(100)  # 100 client handling
    clients = []  # handles the connected clients
    # for each client this is connected by seperate thread

    def client_hadler(client_connection, client_address):
        client_connection.send("connected chat server")
        while True:
            try:
                message = client_connection.recv(2048)
                if message:
                    print(f"[-] {client_address[0]} send a message :")
                    print(f"{message}")
                    message = client_address[0]+' : '+message
                    broadcast(client_connection, message)
                    # sends messsage to other clients on sever
                else:
                    if client_connection in clients:
                        clients.remove(client_connection)
            except:
                continue

    def broadcast(client_connection, message):
        for client in clients:
            if client != client_connection:
                try:
                    client.send(message)
                except:
                    client.close()
                    clients.remove(client)

    while True:
        client_connection, client_address = server_socket.accept()
        # modify here if needs auth in accessing server
        clients.append(client_connection)
        print(f"[+] {client_address[0]} in")
        _thread.start_new_thread(
            client_hadler, (client_connection, client_address))


if __name__ == "__main__":
    print("Starting server at 127.0.0.1:9002 if you want other input function below with args")
    Server()
