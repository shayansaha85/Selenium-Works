import tweet_info as ti
from selenium import webdriver
import time as t
import pyautogui

# DATA
username = ti.username
password = ti.password
url = ti.url
tweet = ti.tweet
driver_path = "driver/geckodriver.exe"

driver = webdriver.Firefox(executable_path=driver_path)
driver.maximize_window()
driver.get(url)
t.sleep(5)

ubox = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input")
pbox = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input")
loginbtn = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div")

ubox.send_keys(username)
pbox.send_keys(password)
loginbtn.click()
t.sleep(5)


tweetbtnbig = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div")
tweetbtnbig.click()

tweetbox = driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div")
tweetbox.send_keys(tweet)
t.sleep(2)

tweetbtn = driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]")
tweetbtn.click()
t.sleep(5)
s = pyautogui.screenshot()
s.save("./test.png")

driver.quit()
