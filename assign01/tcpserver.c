/********************
Lab : Network Lab
Name : Abhinav Kumar
Enroll no.: 510817075
Assignment : 01(Q.01)
*********************/
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
int main()
{
    char message[250] = "This message is send by server to client that connection was successful.\n";
    int server_socket;
    server_socket = socket(AF_INET, SOCK_STREAM, 0); //server endpoint
    struct sockaddr_in server_address;
    server_address.sin_family = AF_INET;
    server_address.sin_port = htons(9002);
    server_address.sin_addr.s_addr = INADDR_ANY;
    bind(server_socket, (struct sockaddr *)&server_address, sizeof(server_address)); //binding socket with address
    listen(server_socket, 5);                                                        //n cnonection will be listened and connected
    int client_socket;
    printf("started server.\n");
    while (1)
    {
        client_socket = accept(server_socket, NULL, NULL); //we will get client's endpoint adress from here
        printf("got request.\n");
        send(client_socket, message, sizeof(message), 0); //message was sent to client
        printf("sent response.\n");
        close(client_socket); //server socket closed
    }
    return 0;
}