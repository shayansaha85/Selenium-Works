from selenium import webdriver
import time


driver= webdriver.Chrome(executable_path="driver/chromedriver.exe")
url= "https://demo.opencart.com/"
driver.get(url)
driver.maximize_window()
time.sleep(5)


usernamebox = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul/li[2]/a")
usernamebox.click()

rbtn= driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul/li[2]/ul/li[1]/a")
rbtn.click()

firstnamebox= driver.find_element_by_xpath("//*[@id=\"input-firstname\"]")
firstnamebox.send_keys("Pranjit")

lastnamebox= driver.find_element_by_xpath("//*[@id=\"input-lastname\"]")
lastnamebox.send_keys("chowdhury")

emailbox=driver.find_element_by_xpath("//*[@id=\"input-email\"]")
emailbox.send_keys("pranjitchow23@gmail.com")

telebox=driver.find_element_by_xpath("//*[@id=\"input-telephone\"]")
telebox.send_keys("936621069")

passbox=driver.find_element_by_xpath("//*[@id=\"input-password\"]")
passbox.send_keys("Pranjit98@")

cpassbox=driver.find_element_by_xpath("//*[@id=\"input-confirm\"]")
cpassbox.send_keys("Pranjit98@")

cbox= driver.find_element_by_xpath("/html/body/div[2]/div/div/form/div/div/input[1]")
cbox.click()

enbox=driver.find_element_by_xpath("/html/body/div[2]/div/div/form/div/div/input[2]")
enbox.click()

driver.save_screenshot("./test.png")
driver.quit()