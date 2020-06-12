/********************
Lab : Network Lab
Name : Abhinav Kumar
Enroll no.: 510817075
Assignment : 03(Q.01)
*********************/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <unistd.h>
#include <netinet/in.h>
#include <netinet/if_ether.h>
#include <asm/byteorder.h>
int main()
{
    struct ethhdr
    {
        unsigned char h_dest[ETH_ALEN];
        unsigned char h_source[ETH_ALEN];
        __be16 h_proto;
    } __attribute__((packed));

    int sock_r;
    sock_r = socket(AF_PACKET, SOCK_RAW, htons(ETH_P_ALL));
    if (sock_r < 0)
    {
        printf("error in socket\n");
        return -1;
    }
    printf("Socket creation successful.\n");
    unsigned char *buffer = (unsigned char *)malloc(65536); //to receive data
    memset(buffer, 0, 65536);
    struct sockaddr saddr;
    struct sockaddr_in source, dest;
    int saddr_len = sizeof(saddr);

    //Receive a network packet and copy in to buffer
    int buflen = recvfrom(sock_r, buffer, 65536, 0, &saddr, (socklen_t *)&saddr_len);
    if (buflen < 0)
    {
        printf("error in reading recvfrom function\n");
        return -1;
    }
    struct ethhdr *eth = (struct ethhdr *)(buffer);
    printf("\nEthernet Header\n");
    printf("\t | -Source Address: % .2X - % .2X - % .2X - % .2X - % .2X - % .2X\n", eth->h_source[0], eth->h_source[1], eth->h_source[2], eth->h_source[3], eth->h_source[4], eth->h_source[5]);
    printf("\t | -Destination Address: % .2X - % .2X - % .2X - % .2X - % .2X - % .2X\n", eth->h_dest[0], eth->h_dest[1], eth->h_dest[2], eth->h_dest[3], eth->h_dest[4], eth->h_dest[5]);
    printf("\t | -Protocol: % d\n", eth->h_proto);
}