from snapshot import take_screenshot
from save_csv import generate_csv
from xpaths import *
import time
from setup import driver
from credentials import *

def launch_site():
    driver.get(url)
    driver.maximize_window()
    time.sleep(3)
    
def save_welcome_text():
    welcome = driver.find_element_by_xpath(welcome_text).text
    file = open(f"markdown/headling.txt", "w")
    file.write(welcome)
    file.close()
    print("==============================================================")
    print(f"String : {welcome} | Saved in : markdown/heading.txt file")
    print("==============================================================")

def lobby_snapshot():
    driver.save_screenshot("snapshots/lobby.png")
    
def enter_the_store():
    driver.find_element_by_xpath(enter_store).click()
    
def landing_page_snapshot():
    driver.save_screenshot("snapshots/landing_page.png")
    
def login():
    driver.find_element_by_xpath(sign_in).click()
    
    driver.find_element_by_name(username).clear()
    driver.find_element_by_name(username).send_keys(uname)
    
    driver.find_element_by_name(password).clear()
    driver.find_element_by_name(password).send_keys(pswd)
    driver.find_element_by_xpath(login_button).click()
    time.sleep(2)
    
def validated_user_snapshot():
    driver.save_screenshot("snapshots/validated_user.png")
    
def snapshots_and_data():
    fish_list = ["Product_ID,Name"]
    dog_list = ["Product_ID,Name"]
    cat_list = ["Product_ID,Name"]
    reptile_list = ["Product_ID,Name"]
    bird_list = ["Product_ID,Name"]
    
    driver.find_element_by_xpath(fish).click()
    take_screenshot(driver,"fish")
    fish_list.append(f'{driver.find_element_by_xpath(product_id_fish_item1).text},{driver.find_element_by_xpath(name_fish_item1).text}')
    fish_list.append(f'{driver.find_element_by_xpath(product_id_fish_item2).text},{driver.find_element_by_xpath(name_fish_item2).text}')
    fish_list.append(f'{driver.find_element_by_xpath(product_id_fish_item3).text},{driver.find_element_by_xpath(name_fish_item3).text}')
    fish_list.append(f'{driver.find_element_by_xpath(product_id_fish_item4).text},{driver.find_element_by_xpath(name_fish_item4).text}')
    generate_csv(fish_list, "fish")
    driver.back()
    
    driver.find_element_by_xpath(dog).click()
    take_screenshot(driver,"dog")
    dog_list.append(f'{driver.find_element_by_xpath(product_id_dog_item1).text},{driver.find_element_by_xpath(name_dog_item1).text}')
    dog_list.append(f'{driver.find_element_by_xpath(product_id_dog_item2).text},{driver.find_element_by_xpath(name_dog_item2).text}')
    dog_list.append(f'{driver.find_element_by_xpath(product_id_dog_item3).text},{driver.find_element_by_xpath(name_dog_item3).text}')
    dog_list.append(f'{driver.find_element_by_xpath(product_id_dog_item4).text},{driver.find_element_by_xpath(name_dog_item4).text}')
    dog_list.append(f'{driver.find_element_by_xpath(product_id_dog_item5).text},{driver.find_element_by_xpath(name_dog_item5).text}')
    dog_list.append(f'{driver.find_element_by_xpath(product_id_dog_item6).text},{driver.find_element_by_xpath(name_dog_item6).text}')
    generate_csv(dog_list, "dog")
    driver.back()
    
    driver.find_element_by_xpath(cat).click()
    take_screenshot(driver,"cat")
    cat_list.append(f'{driver.find_element_by_xpath(product_id_cat_item1).text},{driver.find_element_by_xpath(name_cat_item1).text}')
    cat_list.append(f'{driver.find_element_by_xpath(product_id_cat_item2).text},{driver.find_element_by_xpath(name_cat_item2).text}')
    generate_csv(cat_list, "cat")
    driver.back()
    
    driver.find_element_by_xpath(reptile).click()
    take_screenshot(driver,"reptile")
    reptile_list.append(f'{driver.find_element_by_xpath(product_id_reptile_item1).text},{driver.find_element_by_xpath(name_reptile_item1).text}')
    reptile_list.append(f'{driver.find_element_by_xpath(product_id_reptile_item2).text},{driver.find_element_by_xpath(name_reptile_item2).text}')
    generate_csv(reptile_list, "reptile")
    driver.back()
    
    driver.find_element_by_xpath(bird).click()
    take_screenshot(driver,"bird")
    bird_list.append(f'{driver.find_element_by_xpath(product_id_bird_item1).text},{driver.find_element_by_xpath(name_bird_item1).text}')
    bird_list.append(f'{driver.find_element_by_xpath(product_id_bird_item2).text},{driver.find_element_by_xpath(name_bird_item2).text}')
    generate_csv(bird_list, "bird")
    driver.back()
    
def close_driver():
    driver.quit()