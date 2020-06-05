import requests


def location(ip):
    url = "http://ip-api.com/json/"
    url += ip
    ans = requests.get(url).json()
    print(
        f"client is from {ans['country']}, city {ans['city']} with longitude {ans['lon']} and latitude {ans['lat']}.")


location("")
