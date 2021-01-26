import time 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from env import professional_email, professional_pw, personal_email, personal_pw
from selenium.webdriver.chrome.options import Options

def generate_token(user):
    # fetch the email and password. 
    if user == "professional":
        email = professional_email
        pw = professional_pw
    elif  user == 'personal':
        email = personal_email
        pw = personal_pw

    options = Options()
    options.headless = True
    url = r"https://accounts.google.com/o/oauth2/auth?client_id=438678099331-upimen8ah62h5f8orif95el1f5fhk4cr.apps.googleusercontent.com&redirect_uri=http%3A%2F%2Flocalhost%3A8080%2F&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fgmail.modify&access_type=offline&response_type=code"
    driver = webdriver.Chrome(r"C:\Users\devanshi\Downloads\chromedriver_win32\chromedriver.exe", chrome_options= options)
    driver.get(url)

    # automate the process of entering the email and submitting it. XPath can be used to navigate through elements.
    username = driver.find_element_by_xpath('//*[@id="identifierId"]')
    username.send_keys(email)
    button = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
    button.click()

    time.sleep(5)

    # automated process of entering the password and submitting it.
    password = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    password.send_keys(pw)
    button = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
    button.click()

    # if the user is personal, additional steps are required to authenticate.
    if user == "personal":
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="yDmH0d"]/div[1]/div[1]/a')))
        element.click()

        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="yDmH0d"]/div[1]/div[2]/p[2]/a')))
        element.click()

        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="oauthScopeDialog"]/div[3]/div[1]')))
        element.click()

    # allow the gmail service to access the email provided.
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="submit_approve_access"]/div/button')))
    element.click()
        



  
