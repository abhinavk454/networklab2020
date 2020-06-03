/********************
Lab : Network Lab
Name : Abhinav Kumar
Enroll no.: 510817075
Assignment : 02(Q.02)
*********************/

#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <time.h>
#include <unistd.h>
#include <netinet/in.h>

int main()
{
    char res[100];
    int server_socket, response, n;
    struct tm *ptr;
    time_t lt;
    server_socket = socket(AF_INET, SOCK_DGRAM, 0);    //server  socket creation
    struct sockaddr_in server_address, client_address; //allocating address for server and clients
    server_address.sin_family = AF_INET;
    server_address.sin_port = htons(9002); //16bit to port
    server_address.sin_addr.s_addr = INADDR_ANY;
    lt = time(NULL);
    ptr = localtime(&lt);
    printf("starting UPD server on localhost at ");
    printf("%s", asctime(ptr));
    bind(server_socket, (struct sockaddr *)&server_address, sizeof(server_address)); //binding socket at adrress to listen
    while (1)
    {
        n = sizeof(client_address);
        response = recvfrom(server_socket, res, sizeof(res), 0, (struct sockaddr *)&client_address, &n);
        res[response] = '\0';
        printf("got %s request\n", res);
        sendto(server_socket, "pong", 1024, 0, (struct sockaddr *)&client_address, sizeof(client_address));
    }
    return 0;
}