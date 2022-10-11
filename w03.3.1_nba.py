import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime

options = Options()
webdriver_service = Service(r"C:\Users\Admin\Downloads\chromedriver_win32 (1)\chromedriver.exe")
driver = webdriver.Chrome(service=webdriver_service, options=options)

driver.get("https://www.nba.com/schedule?pd=false&region=1")
driver.implicitly_wait(5)
element_to_click=driver.find_element(By.ID,"onetrust-accept-btn-handler")
element_to_click.click()
element_to_save=driver.find_element(By.XPATH,"//div/div/div/div/h4")

f=open('new_result_file00.txt','w')
f.write(element_to_save.text)
f.write("\n")
f.write(str(datetime.today()))
myList=[]
myList.append(1)

wait = WebDriverWait(driver, 10)
elements_to_save=wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//*[@data-id='nba:schedule:main:team:link']")))

i=1

for element in elements_to_save:

    try:
        driver.execute_script("arguments[0].scrollIntoView();", element)
        f.write(" ")
        f.write(element.text)
        myList.append(element.text)
    except Exception as e:
        time.sleep(5)
        print("err",i)
        i=i+1
    f.write(" \n ")
    f.write(str(datetime.today()))

f.close()

time.sleep(1)
driver.get("https://www.nba.com/stats/teams/traditional")

season_click=wait.until(EC.visibility_of_all_elements_located((By.XPATH,"//option[@value='2021-22']")))
season_click[0].click()

d=1
teamStats = []
for d in range(len(myList)):
    xpath_template="//tr[contains(.,'{0}')]"
    xpath=xpath_template.format(myList[d])
    try:
        tr=driver.find_element(By.XPATH,xpath)
    except Exception as e:
        teamStats.append(myList[d])
        teamStats.append("new-comer-team")

    print("-",teamStats)
    for i in range(7):
        a=i+1
        teamStats.append(tr.find_element(By.XPATH, ".//td["+str(a)+"]").text)
        print("--", teamStats)

print("---",teamStats)
driver.quit()
