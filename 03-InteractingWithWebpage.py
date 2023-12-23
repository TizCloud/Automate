# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
 
# create webdriver object
driver = webdriver.Firefox()
 
# get web page
driver.get("http://www.python.org")
 
# get element
element = driver.find_element(By.ID, "id-search-field")
 
# send keys
element.send_keys("pycon")

