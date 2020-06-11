##########################
# Lab : Network Lab      #
# Name : Abhinav Kumar   #
# Enroll no.: 510817075  #
# Assignment : 06(Q.01)  #
##########################

import requests
from pprint import pprint
try:
    from scrapy import Selector
except ImportError:
    print("run 'pip3 install scrapy' in terminal")


def scrapper(url):
    # extract response
    html = requests.get(url).content
    sel = Selector(text=html)
    # select title
    ans = sel.xpath('//title').extract()
    if ans:
        print(f"[+] Title :\n{ans}")
    # selects links
    links = sel.xpath('//link').extract()
    if links:
        print(f"[+] Links :\n{links}")
    # select headers
    headers = sel.xpath('//h1').extract()
    if headers:
        print(f"[+] Headers :\n{headers}")
    # selects texts
    para = sel.xpath('//p').extract()
    if para:
        print(f"[+] Paragraphs :\n{para}")


if __name__ == "__main__":
    url = input("Enter url to crawl :")
    scrapper(url)
