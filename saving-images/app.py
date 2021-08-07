import urllib.request

from selenium import webdriver
import time as t
 

driver = webdriver.Firefox(executable_path="C:\\Users\\Shayan Saha\\Desktop\\selenium-tutorial\\linkedin-signin\\driver\\geckodriver.exe")

driver.get('https://www.google.com/')
t.sleep(5)
 

# get the image source

img = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/img')

src = img.get_attribute('src')

 

# download the image

urllib.request.urlretrieve(src, "captcha.png")

driver.close()