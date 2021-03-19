from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.binance.com/en/trade/DOGE_USDT")

thing = driver.find_element_by_class_name("css-uliqdc")
print(thing)