##########################
# Lab : Network Lab      #
# Name : Abhinav Kumar   #
# Enroll no.: 510817075  #
# Assignment : 05(Q.01)  #
##########################


import socket
import requests


def location(ip):  # this section will find location of client via api request
    url = "http://ip-api.com/json/"
    if ip != '127.0.0.1':
        url += ip
    ans = requests.get(url).json()
    print(
        f"client's public ip is {ans['query']} surfing from from {ans['country']}, state {ans['regionName']}, city {ans['city']} with longitude {ans['lon']} and latitude {ans['lat']}.\n")
    if ans['isp']:
        print(f"client's ISP is {ans['isp']}\n\n")
    return float(ans['lon']), float(ans['lat'])


def tcpserver(host=socket.gethostname(), port=9002):
    # started a tcp socketendpoint
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))  # allocate address to server
    server_socket.listen(5)  # listen for request
    print("\n\n\t\t######################################################################################################")
    print(
        f"\t\t# started server at : http://{host}:{port} please open this URL in browser to see location in map. #")
    print("\t\t######################################################################################################\n\n")
    try:
        while True:
            client_socket, client_address = server_socket.accept()  # accepts requests
            print("got request from a client whose info is below : ")
            try:
                # getting location via api
                client_lon, client_lat = location(str(client_address[0]))
            except Exception:
                print("connection error occured during getting location")
            # decoding readable message coded message
            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            # this will automaticaly redirect client to its ip location
            #data += f"<head><meta http-equiv='refresh' content='0; url=https://www.google.com/maps/search/{client_lat},{client_lon}'></head>"
            # this will take via serevr page to
            data += f"<html><head></head><body style='background-color:#659DBD'><div style='display:box;text-align:center;color:#659DBD;background-color:#E27D60;border:3px solid #41B3A3;border-radius:100px;margin:auto;padding:10px'><h3>CLICK TEXT BELOW TO GO TO YOUR IP LOCATION IN GMAP<h3></div><div style='display:box;text-align:center;color:black;background-color:#8D8741;border:3px solid #FBEEC1;border-radius:100px;margin:auto;padding:10px'><a style='color:#659DBD' href='https://www.google.com/maps/search/{client_lat},{client_lon}'><h3>GO TO GMAP<h3></a></div></body></html>"
            client_socket.sendall(data.encode())
            #print(f"sent response to {client_address[0]}:{client_address[1]}")
            client_socket.shutdown(socket.SHUT_WR)  # closing client connection
    except KeyboardInterrupt:
        print("Closing Server...")


if __name__ == "__main__":
    # if want to start server on certain address and port
    # then have to pass address and port as argument by default it's set to loopback addr
    tcpserver(host='127.0.0.1')

# i have used fstring in this assignment if during execution of this code error happens
# then python3 on your system needs upgrade means it's below 3.6
