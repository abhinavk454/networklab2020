import socket
MAX_SIZE_BYTES = 65535 # Mazimum size of a UDP datagram
def client(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    hosts = []
    while True:
        host = input('Input host address:' )
        hosts.append((host,port))
        message = input('Input message to send to server:' )
        data = message.encode('ascii')
        s.sendto(data, (host, port))
        print('The OS assigned the address {} to me'.format(s.getsockname()))
        data, address = s.recvfrom(MAX_SIZE_BYTES)
        text = data.decode('ascii')
        if(address in hosts):
            print('The server {} replied with {!r}'.format(address, text))
            hosts.remove(address)
        else:
            print('message {!r} from unexpected host {}!'.format(text, address))