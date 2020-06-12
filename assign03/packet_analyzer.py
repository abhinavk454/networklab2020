##########################
# Lab : Network Lab      #
# Name : Abhinav Kumar   #
# Enroll no.: 510817075  #
# Assignment : 03(Q.01)  #
##########################


# works on unix/linux
import socket
import struct
import binascii


class PacketAna():
    def __init__(self, raw_socket):
        self.raw_socket = raw_socket
        self.packet = self.raw_socket.recvfrom(2048)

    def ethr_ana(self):
        # ether header
        ethrow_header = self.packet[0][0:14]
        # 6destMac6hostMac2etherType
        ether_header = struct.unpack("!6s6s2s", ethrow_header)
        print(f"\t |-Source address = {binascii.hexlify(ether_header[0])}")
        print(
            f"\t |-Destination address = {binascii.hexlify(ether_header[1])}")
        print(f"\t |-Protocol = {binascii.hexlify(ether_header[2])}")

    def ip_ana(self):
        ipro_header = self.packet[0][14:34]
        ip_header = struct.unpack("!12s4s4s", ipro_header)
        # networktoascii
        print(f"\t |-Source IP is = {socket.inet_ntoa(ip_header[1])}")
        print(f"\t |-Destination IP = {socket.inet_ntoa(ip_header[2])}")

    def tcp_ana(self):
        tcpro_header = self.packet[0][34:54]
        tcp_header = struct.unpack("!HH16s", tcpro_header)
        print(f"\t |-Source port = {tcp_header[0]}")
        print(f"\t |-Destination port = {tcp_header[1]}")


if __name__ == "__main__":
    raw_socket = socket.socket(
        family=socket.PF_PACKET, type=socket.SOCK_RAW, proto=socket.htons(0x0800))
    ana = PacketAna(raw_socket)
    print("\t***********PACKET**FROM**RAWSOCKET***********")
    print(f"\t |-({ana.packet})")
    print("\n\t***********FROM**ETH**HEADER**ANALYSIS************")
    ana.ethr_ana()
    print("\n\t***********FROM**IP**HEADER**ANALYSIS**********")
    ana.ip_ana()
    print("\n\t***********FROM**TCP**HEADER**ANALYSIS************\n")
    ana.tcp_ana()
