##########################
# Lab : Network Lab      #
# Name : Abhinav Kumar   #
# Enroll no.: 510817075  #
# Assignment : 07(Q.01)  #
##########################


import socket
import random
import struct
import time


class traceroute():
    def __init__(self, dst, hops=30):
        # destination
        self.dst = dst
        # hoping limmit
        self.hops = hops
        self.ttl = 1
        # Pick up a random port in the range 33434-33534 which is used by defult fort traceroute
        self.port = random.choice(range(33434, 33535))

    def run(self):
        try:
            dst_ip = socket.gethostbyname(self.dst)
        except socket.error as e:
            raise IOError(f'Unable to resolve {self.dst}: {e}')
        print(
            f"tracing router b/w self to {self.dst} ({dst_ip}), with {self.hops} hops")
        while True:
            startTimer = time.time()
            receiver = self.create_receiver()
            sender = self.create_sender()
            sender.sendto(b'', (self.dst, self.port))
            addr = None
            try:
                data, addr = receiver.recvfrom(1024)
                entTimer = time.time()
            except socket.error:
                pass
            finally:
                receiver.close()
                sender.close()
            if addr:  # if router has visible address
                timeCost = round((entTimer - startTimer) * 1000, 2)
                print('{:<4} {} {} ms'.format(self.ttl, addr[0], timeCost))
                if addr[0] == dst_ip:
                    break
            else:  # if no visible addr
                print('{:<4} #'.format(self.ttl))
            self.ttl += 1
            if self.ttl > self.hops:
                break

    def create_receiver(self):
        # receiver socket is of type RAW
        # raw socket so sudo needs when we run this program
        recv_s = socket.socket(family=socket.AF_INET,
                               type=socket.SOCK_RAW, proto=socket.IPPROTO_ICMP)
        timeout = struct.pack("ll", 5, 0)
        recv_s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVTIMEO, timeout)
        try:
            recv_s.bind(('', self.port))
        except socket.error as e:
            raise IOError(f"unable to bind {e}")
        return recv_s

    def create_sender(self):
        # sender socket is of type UDP
        send_s = socket.socket(
            socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        send_s.setsockopt(socket.SOL_IP, socket.IP_TTL, self.ttl)
        return send_s


if __name__ == "__main__":
    # need to change here if custom hops needed
    print("Run with sudo since RAW socket is used as receving socket.\n")
    dst = input("Enter the destination address :")
    tracer = traceroute(dst=dst)
    tracer.run()
