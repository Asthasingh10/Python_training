from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver
driver = webdriver.Chrome()
q="laptop"
driver.get(f"https://www.amazon.in/s?k={q}&crid=DHQI5P2TPW4V&sprefix=lapto%2Caps%2C291&ref=nb_sb_noss_2")

elem =driver.find_elements(By.CLASS_NAME, "puisg-col-inner")
print(elem)

driver.close()