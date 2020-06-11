/********************
Lab : Network Lab
Name : Abhinav Kumar
Enroll no.: 510817075
Assignment : 06(Q.01)
*********************/

#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <curl/curl.h>
//sudo apt-get install  libcurl4-openssl-dev if error occurs in lcurl
//cc web_crawler.c -o web_crawler -lcurl to compile and ./web_crawler url to run
int main(int argc, char *argv[])
{
    CURL *curl;
    CURLcode res;
    curl = curl_easy_init();
    if (curl)
    {
        curl_easy_setopt(curl, CURLOPT_URL, argv[1]);
        curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1L);
        // Perform the request
        res = curl_easy_perform(curl);
        //error handling
        if (res != CURLE_OK)
            fprintf(stderr, "curl_easy_perform() failed: %s\n", curl_easy_strerror(res));
        //cleanup
        curl_easy_cleanup(curl);
    }
    return 0;
}