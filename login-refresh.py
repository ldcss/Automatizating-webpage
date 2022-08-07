from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from time import time

def xpathWrite(xpath, key):
    elem = browser.find_element(By.XPATH, xpath)
    elem.clear()
    elem.send_keys(key)

def xpathClickNotRobot(xpath):
    elem = browser.find_element(By.XPATH, xpath)
    browser.execute_script("arguments[0].click();", elem)
    elem.send_keys(Keys.RETURN)

def xpathClick(xpath):
    elem = browser.find_element(By.XPATH, xpath)
    elem.click()

def loopRefresh(minLog, secRefresh):
    minLog = minLog * 60
    t_end = time() + minLog

    while time() < t_end:
        xpathClick('//i[@class="fa fa-globe fa-2x"]')
        sleep(secRefresh) #espera 90s para clicar no botao

def closingTabs():
    for handle in browser.window_handles: #closing all tabs
        browser.switch_to.window(handle)
        browser.close() 

if __name__ == "__main__":
    while True:
        browser = webdriver.Firefox()
        browser.get("#URL-HERE")
        sleep(1)
        xpathWrite("//input[@id='xxlogin']", "#LOGIN-HERE")
        xpathWrite("//input[@id='xxsenha']", "#PASSWORD-HERE")
        xpathClickNotRobot("//input[@class='is-checkradio has-background-color is-success']") #Clicking not-robot button
        sleep(2)
        browser.get("#URL-CLIENT-PAGE-HERE")
        xpathClick('//input[@id="checkAll"]')
        xpathClickNotRobot('//input[@id="check2All"]') #accessing all clients
        sleep(3)
        xpathClick('//i[@class="fa fa-globe fa-2x"]') #showing all clients in maps
        loopRefresh(0.5, 10)#get the minute for login time, then close the browser and login again. and getting the seconds for refreshing the map
        closingTabs()
