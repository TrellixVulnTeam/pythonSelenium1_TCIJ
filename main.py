import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install())
url = "https://stackoverflow.com/questions/53657215/running-selenium-with-headless-chrome-webdriver"
driver.get(url)

time.sleep(2)

h1 = driver.find_element_by_xpath("//h1[@itemprop='name']").text
print(h1)

assert h1 == "Running Selenium with Headless Chrome Webdriver"
print("Test Passed")