from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# Set up the WebDriver
driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
# Extract dynamic content
elem =driver.find_elements(By.TAG_NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No result found" not in driver.page_source
driver.close()