import time
import textwrap
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def searchGoogle(query):
    fox = webdriver.Firefox()
    fox.get('https://www.google.com/search?q=' + query)
    foxBoxx = fox.find_element_by_class_name('g')
    foxBox = textwrap.fill(foxBoxx.text)
    fox.quit()
    print(foxBox)
    
