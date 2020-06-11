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
    int network_socket;
    network_socket = socket(AF_INET, SOCK_STREAM, 0); //one end point sock_stream for tcp
    struct sockaddr_in server_address;                //creates server address
    server_address.sin_family = AF_INET;
    server_address.sin_port = htons(9002);       //htons convert int to port data type
    server_address.sin_addr.s_addr = INADDR_ANY; //assingns address to server
    int connection_status = connect(network_socket, (struct sockaddr *)&server_address, sizeof(server_address));
    if (connection_status == -1)
    {
        printf("Connection error");
    }
    printf("Request sent to server \n");
    char recv_data[250];
    recv(network_socket, &recv_data, sizeof(recv_data), 0); //flag is set to 0
    printf("Server's response :%s\n", recv_data);
    close(network_socket); //closes the endpoint so other process can use it
    return 0;
}
