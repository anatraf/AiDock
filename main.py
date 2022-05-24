from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
service1 = Service(r"C:\Users\Anat\Documents\ענת\קורס QA\selenium\chromedriver.exe")
driver = webdriver.Chrome(service=service1)
from selenium.webdriver.common.by import By
#can use the keybord of the computer
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver.get("https://www.google.co.il")
# in case an element is nit found - define a 10 seconds timeout
driver.implicitly_wait(10)

# write a text in google search line and store it in a vairable
gmail_botton = driver.get(r'https://accounts.google.com/signin/v2/identifier?continue='+\
    'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1'+\
    '&flowName=GlifWebSignIn&flowEntry = ServiceLogin')
loginBox = driver.find_element_by_xpath('//*[@id ="identifierId"]')
loginBox.send_keys("anataidockproject@gmail.com")
nextButton = driver.find_elements_by_xpath('//*[@id ="identifierNext"]')
nextButton[0].click()
passWordBox = driver.find_element_by_xpath('//*[@id ="password"]/div[1]/div / div[1]/input')
passWordBox.send_keys("Anataidock1")
nextButton = driver.find_elements_by_xpath('//*[@id ="passwordNext"]')
nextButton[0].click()
sleep(20)
num_of_mails = driver.find_element_by_xpath('//*[@id=":9t"]/span/span[1]/span[2]')
num_of_mails[0].click()
print(num_of_mails)

subject_name = driver.find_element(By.CLASS_NAME,"bog")
print(subject_name)

sender_name = driver.find_element(By.CLASS_NAME,"yW")
print(sender_name)

