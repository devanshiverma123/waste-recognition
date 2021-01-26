import time
# importing webdriver from selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
 
# Here Chrome  will be used
driver = webdriver.Chrome(r"C:\Users\devanshi\Downloads\chromedriver_win32\chromedriver.exe")
 
# URL of website
url = "https://developers.google.com/gmail/api/quickstart/python"
 
# Opening the website
driver.get(url)
 
# getting the button by class name
button =  driver.find_element_by_xpath('//*[@id="gc-wrapper"]/main/devsite-content/article/div[2]/p[4]/devsite-api-getstarted/a')
button.click()

email = ""

username = driver.find_element_by_xpath('//*[@id="identifierId"]')
username.send_keys(email)

button = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
button.click()
# driver.implicitly_wait(10)
time.sleep(5)
pw = ''
password = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
# password = driver.find_element_by_class_name('whsOnd zHQkBf')
password.send_keys(pw)

button = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
button.click()
time.sleep(5)
button = driver.find_element_by_xpath('//*[@id="gc-wrapper"]/main/devsite-content/article/div[2]/p[4]/devsite-api-getstarted/a')
button.click()
time.sleep(10)

try:
    
    iframe = driver.find_element_by_xpath("/html/body/div[2]/devsite-dialog/div/div[2]/iframe")
    driver.switch_to.frame(iframe)
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/hen-flow/div/div/div[2]/div[2]/button[2]')))
    element.click()
    print("NEXT SUCCESSFUL(1)")

    element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/hen-flow/div/hen-oauth-editor/div/form/div[2]/div[2]/button[2]')))
    element.click()
    print("Create")

    element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/hen-flow/div/hen-success-page/div[2]/div[2]/ng-container/div/a')))
    element.click()
    print("Download")

    element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/hen-flow/div/hen-success-page/div[3]/div[2]/button')))
    element.click()
    print("Done")
    
except:
    print("Not able to find Element")

