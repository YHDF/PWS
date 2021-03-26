import re
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from amazon import *

def init(id_group, link, product_class) :
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)
    driver.get(link)
    #assert "Python" in driver.title
    elem = driver.find_elements_by_css_selector(product_class)
    products = extraction(id_group, elem)
    driver.quit()
    return products
