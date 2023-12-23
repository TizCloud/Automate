# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

# create webdriver object
driver = webdriver.Firefox()

# enter keyword to search
keyword = "pycon"

driver.get("http://www.python.org")

# get element 
element = driver.find_element(By.NAME, "q")

# print complete element
print(element)
