import requests
from bs4 import BeautifulSoup
import ebay as ebay


def init(id_group, link, group_class) :
    request = requests.get(link)
    soup = BeautifulSoup(request.text, 'lxml')
    result = soup.find_all("li", class_=group_class)
    products = ebay.extraction(id_group, result)
    return products
