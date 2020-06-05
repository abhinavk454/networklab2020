#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <unistd.h>
#include <netinet/in.h>
#include <netinet/if_ether.h>
#include <asm/byteorder.h>
struct iphdr
{
#if defined(__LITTLE_ENDIAN_BITFIELD)
    __u8 ihl : 4,
        version : 4;
#elif defined(__LITTLE_ENDIAN_BITFIELD)
    __u8 version : 4,
        ihl : 4;
#else
#error "Error"
#endif
    __u8 tos;
    __be16 tot_len;
    __be16 id;
    __be16 frag_off;
    __u8 ttl;
    __u8 protocol;
    __sum16 check;
    __be32 saddr;
    __be32 daddr;
};
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
    unsigned short iphdrlen;
    struct iphdr *ip = (struct iphdr *)(buffer + sizeof(struct ethhdr));
    memset(&source, 0, sizeof(source));
    source.sin_addr.s_addr = ip->saddr;
    memset(&dest, 0, sizeof(dest));
    dest.sin_addr.s_addr = ip->daddr;
    FILE *log_txt;
    log_txt = fopen("data.txt", "w+");
    fprintf(log_txt, "\t | -Version: % d\n", (unsigned int)ip->version);

    fprintf(log_txt, "\t | -Internet Header Length: % d DWORDS or % d Bytes\n", (unsigned int)ip->ihl, ((unsigned int)(ip->ihl)) * 4);

    fprintf(log_txt, "\t | -Type Of Service: % d\n", (unsigned int)ip->tos);

    fprintf(log_txt, "\t | -Total Length: % d Bytes\n", ntohs(ip->tot_len));

    fprintf(log_txt, "\t | -Identification: % d\n", ntohs(ip->id));

    fprintf(log_txt, "\t | -Time To Live: % d\n", (unsigned int)ip->ttl);

    fprintf(log_txt, "\t | -Protocol: % d\n", (unsigned int)ip->protocol);

    fprintf(log_txt, "\t | -Header Checksum: % d\n", ntohs(ip->check));

    fprintf(log_txt, "\t | -Source IP: % s\n", inet_ntoa(source.sin_addr));

    fprintf(log_txt, "\t | -Destination IP: % s\n", inet_ntoa(dest.sin_addr));
}