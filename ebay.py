from bs4 import BeautifulSoup
from product import Product
import re


items_list = [0]*0

def extraction(id_group, result) :
    for product in result :
        #produt = product.find("div", class_="s-item__image-wrapper").find("div", class_="s-item__image-helper")
        name = product.find("h3", attrs={"class" : "s-item__title"})
        link = product.find("a" , attrs={"class" : "s-item__link"})['href']
        img_link = product.find("img" , attrs={"class" : "s-item__image-img"})
        img_link = img_link['src'] if img_link['src'].find("gif") < 0 else img_link['data-src']
        price = product.find("span", attrs={"class" : "s-item__price"})
        price = re.findall('(\d\d,\d\d\d|\d,\d\d\d|\d\d\d|\d\d)', price.getText())
        price = int(price[0].replace(',', ''))
        item = Product(id_group, name.getText(), link, img_link, price)
        items_list.append(item)
    return items_list
