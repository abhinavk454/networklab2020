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
#include <sys/time.h>
#include <time.h>
#include <unistd.h>
#include <netinet/in.h>

int main()
{
    time_t start, end;
    struct timeval stop1, start1;
    float total_time = 0;
    for (int i = 0; i < 10; i++)
    {
        int client_socket, connection_status;
        char res[100];
        struct tm *ptr;
        time_t lt;
        client_socket = socket(AF_INET, SOCK_DGRAM, 0); //client socket creation
        struct sockaddr_in server_address;
        server_address.sin_family = AF_INET;
        server_address.sin_port = htons(9002); //16bit to port
        server_address.sin_addr.s_addr = INADDR_ANY;
        lt = time(NULL);
        ptr = localtime(&lt);
        printf("sending ping no: %d to server at %s", i + 1, asctime(ptr));
        connection_status = connect(client_socket, (struct sockaddr *)&server_address, sizeof(server_address)); //connecting toserver
        if (connection_status < 0)
        {
            printf("connection error\n");
            exit(0);
        }
        gettimeofday(&start1, NULL);
        sendto(client_socket, "ping", 1024, 0, (struct sockaddr *)NULL, sizeof(server_address)); //sending ping
        recvfrom(client_socket, res, sizeof(res), 0, (struct sockaddr *)NULL, NULL);             //getting response
        gettimeofday(&stop1, NULL);
        total_time = total_time + stop1.tv_usec - start1.tv_usec;
        close(client_socket); //closing client connection
        printf("%s\n", res);
    }
    printf("The average RTT for 10 ping is %.4fus\n", total_time / 10);
    return 0;
}