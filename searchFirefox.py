import time
import textwrap
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def searchGoogle(query):
    fox = webdriver.Firefox()
    fox.get('https://www.google.com/search?q=' + query)
    foxBoxx = fox.find_element_by_class_name('g')
    foxBox = textwrap.fill(foxBoxx.text)
    print(foxBox)
    time.sleep(0) #@Cole Papa. If you want the browser to stay open, you can keep this line of code. Otherwise, just delete it.
    fox.quit()
    
