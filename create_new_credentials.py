import time 
from selenium import webdriver
from env import professional_email, professional_pw
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
 


url = "https://console.cloud.google.com/apis/credentials?project=quickstart-1609754216870&folder=&organizationId="
options = webdriver.ChromeOptions()
options.add_argument(r"download.default_directory=C:\Users\devanshi\Desktop\Python\gmail_dropbox\quickstart")
driver = webdriver.Chrome(r"C:\Users\devanshi\Downloads\chromedriver_win32\chromedriver.exe", chrome_options=options)

driver.get(url)

#email
username = driver.find_element_by_xpath('//*[@id="identifierId"]')
username.send_keys(professional_email)
button = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
button.click()

time.sleep(5)

#password
password = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
password.send_keys(professional_pw)
button = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
button.click()

time.sleep(15)
#create credentials
button = driver.find_element_by_xpath('//*[@id="action-bar-create-button"]/span[1]')
button.click()

#auth
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cdk-overlay-0"]/div/div/div/cfc-menu-section[1]/div/cfc-menu-item[2]/a/div[1]/div/div[1]/div[2]')))
element.click()

time.sleep(5)
#dropdown options
button = driver.find_element_by_xpath('//*[@id="_0rif_mat-form-field-label-1"]')
button.click()

#desktop app
time.sleep(5)
button = driver.find_element_by_xpath('//*[@id="_0rif_mat-option-5"]/span')
button.click()

#create
button = driver.find_element_by_xpath('//*[@id="main"]/div/div/central-page-area/div/div/pcc-content-viewport/div/div/pangolin-home/cfc-router-outlet/div/ng-component/cfc-single-panel-layout/cfc-panel-container/div/div/cfc-panel/div/div/cfc-panel-body/cfc-virtual-viewport/div[1]/div/form/services-oauth-client-form/form/ace-progress-button/div/button/span[1]')
button.click()

# ok credentials
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-dialog-0"]/highlight-client-dialog/div[2]/button')))
element.click()

#download
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cfc-table-caption-4-row-0"]/td[7]/cfc-download-text/button')))
element.click()

