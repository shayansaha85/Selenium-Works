from selenium import webdriver
import time
import pyautogui

driver = webdriver.Firefox(executable_path="driver/geckodriver.exe")

url = "https://www.linkedin.com/"

driver.get(url)
driver.maximize_window()
time.sleep(5)

usernamebox = driver.find_element_by_xpath("//*[@id=\"session_key\"]")
usernamebox.send_keys("shayansaha.work@gmail.com")

passbox = driver.find_element_by_xpath("//*[@id=\"session_password\"]")

# ENTER YOUR PASSWORD HERE
passbox.send_keys("**********")

signinbtn = driver.find_element_by_xpath("/html/body/main/section[1]/div[2]/form/button")
signinbtn.click()

time.sleep(10)

profile = driver.find_element_by_xpath("/html/body/div[6]/div[3]/div/div/div[2]/div/div/div/div[1]/div[1]/a/div[2]")
profile.click()

time.sleep(5)

biotext = driver.find_element_by_xpath("/html/body/div[6]/div[3]/div/div/div/div/div[3]/div/div/main/div/section[1]/div[2]/div[2]/div/div[2]")
v = biotext.text

f = open("bio.txt", "w")
f.write(v)
f.close()



driver.quit()