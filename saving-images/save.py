import urllib.request
from selenium import webdriver
import time
import os

driver = webdriver.Firefox(executable_path="C:\\Users\\Shayan Saha\\Desktop\\selenium-tutorial\\linkedin-signin\\driver\\geckodriver.exe")
driver.get("https://www.google.com/")
time.sleep(3)

img = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/img")
source = img.get_attribute('src')
os.system("mkdir logo")
urllib.request.urlretrieve(source, "logo/googlelogo.png")
driver.close()