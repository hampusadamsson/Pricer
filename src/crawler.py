from bs4 import BeautifulSoup
import requests
import json


def crawl_site(url):
    uri = requests.get(url)
    data = uri.text
    soup = BeautifulSoup(data, features="html.parser")
    return soup


def get_koksbryggeriet():
    url = "https://www.koksbryggeriet.se/sv/artiklar/grainfather-connect-bryggverk-25-l.html"
    soup = crawl_site(url)
    priceRaw = soup.find("span", {"class": "PrisREA"}).get_text()
    cost = priceRaw.split()[0]
    price = int(cost)
    return price


def get_hembryggeriet():
    url = "https://www.hembryggeriet.se/grainfather-connect-bryggverk-30l"
    soup = crawl_site(url)
    rawJson = soup.find("script", {"type": "application/ld+json"}).get_text()
    jsonObj = json.loads(rawJson)[0]
    cost = jsonObj["offers"]["price"]
    price = int(cost)
    return price


def get_pgw():
    url = "https://www.pgw.se/grainfather-bryggverk-25-l.html"
    soup = crawl_site(url)
    rawJson = soup.find("span", {"class": "price"}).get_text()
    cost = "".join([t for t in rawJson if t.isnumeric()])
    price = int(cost)
    return price


def crawl_site_by_name(name):
    name = name.lower()
    if name == "pgw":
        return get_pgw()
    elif name == "hembryggeriet":
        return get_hembryggeriet()
    elif name == "koksbryggeriet":
        return get_koksbryggeriet()
    else:
        return "Error"
