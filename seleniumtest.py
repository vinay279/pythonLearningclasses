
import os
from selenium import webdriver

chromedriver = "D:\\New folder\\chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://stackoverflow.com")
driver.maximize_window()

print(driver.title())