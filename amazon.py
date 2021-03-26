import re
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from product import Product


items_list = [0]*0

def extraction(id_group,elem) :
    for product in elem :
        name = product.find_element_by_css_selector(".a-size-medium.a-color-base.a-text-normal")
        link = product.find_element_by_css_selector(".a-link-normal.a-text-normal")
        link = link.get_attribute('href')
        img_link = product.find_element_by_css_selector(".s-image")
        img_link = img_link.get_attribute('src')
        try :
            price = product.find_element_by_css_selector(".a-price-whole")
        except NoSuchElementException :
            continue
        price = re.findall('(\d\d\s\d\d\d|\d\s\d\d\d|\d\d\d|\d\d)', price.text)[0]
        price = price.replace("\u202f", "")
        price = int(price)
        item = Product(id_group,name.text, link, img_link, price)
        items_list.append(item)
    return items_list
