from selenium import webdriver as w
from selenium.webdriver.chrome.options import Options

import roll_numbers as rn
import time as t
import pandas as pd


roll = []
reg = []
column_names = "Name,Roll_No.,Reg_No.,Marks,Percentage(%),Grade"
results = []


for x in rn.roll_numbers:
    roll.append(x.split("/")[0])
    reg.append(x.split("/")[-1])

length = len(roll)

for i in range(length):
    rno = roll[i]
    regno = reg[i]
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    #driver = w.Chrome(options=chrome_options)
    driver = w.Chrome(executable_path="driver/chromedriver.exe", options=chrome_options)
    link = "https://tbresults.tripura.gov.in/"
    driver.get(link)
    driver.maximize_window()
    t.sleep(3)

    result_type = driver.find_element_by_xpath("/html/body/div[2]/center/table/tbody/tr[1]/td[2]/div/table/tbody/tr[4]/td[3]/a/b")
    result_type.click()

    roll_no = driver.find_element_by_name("rno")
    reg_no = driver.find_element_by_name("regno")

    roll_no.clear()
    reg_no.clear()
    roll_no.send_keys(rno)
    reg_no.send_keys(regno)

    show_result = driver.find_element_by_name("B1")
    show_result.click()

    name = driver.find_element_by_xpath("//*[@id=\"AutoNumber1\"]/tbody/tr[3]/td[2]").text
    total_marks = driver.find_element_by_xpath("/html/body/center/font/div/center[2]/center/table/tbody/tr[2]/td[1]/p").text
    grade = driver.find_element_by_xpath("/html/body/center/font/div/center[2]/center/table/tbody/tr[2]/td[2]/p").text
    percentage = round( (float(total_marks)/5), 2)
    print(type(name))
    data = f"{name},{rno},{regno},{total_marks},{percentage},{grade}"
    results.append(data)
    driver.quit()


# print(results)
details = {}

fields = column_names.split(",")

for x in fields:
    details[x] = []

for x in results:
    for i in range(6):
        details[fields[i]].append(x.split(",")[i])

df = pd.DataFrame(details)
df.to_csv("results.csv", index=False)
df.to_html("results.html")

print()
print("========================================")
print("DONE")
print("========================================")
print()