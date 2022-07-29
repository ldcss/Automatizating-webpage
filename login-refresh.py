from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def xpathWrite(xpath, key):
    elem = browser.find_element(By.XPATH, xpath)
    elem.clear()
    elem.send_keys(key)

def xpathClick(xpath):
    elem = browser.find_element(By.XPATH, xpath)
    browser.execute_script("arguments[0].click();", elem)
    elem.send_keys(Keys.RETURN)

def refreshMap(): #refresh the map every minute
    t_end = time.time() + 20
    while time.time() < t_end:
        xpathClick('//i[@class="fa fa-globe fa-2x"]')
        print('teste3')

while True:
    #ABRE O BROWSER
    browser = webdriver.Firefox()
    browser.get("URL")
    time.sleep(1)
    original_window = browser.current_window_handle
    xpathWrite("//input[@id='xxlogin']", "login")
    xpathWrite("//input[@id='xxsenha']", "password")
    #clicking in the no-robot button
    xpathClick("//input[@class='is-checkradio has-background-color is-success']") 
    time.sleep(2)
    ###AFTER LOGIN
    browser.get("URL_CLIENT_SESSION")
    xpathClick('//input[@id="checkAll"]') #clicking on all clients
    xpathClick('//input[@id="check2All"]') #clicking in all pages