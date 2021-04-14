from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup, NavigableString, Tag 
import pandas as pd
import os
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
from webdriver_manager.chrome import ChromeDriverManager
from urllib.request import Request, urlopen


TARGET_URL =  'https://www.just-eat.co.uk/restaurants-chasingdragon-willesdennw10/menu'
TARGET_URL1 = "https://hide.me/en/proxy"

#MAIN
def main():

    #MAKE A DRIVER SESSION
    
    chrome_options = Options()
    prefs = {"profile.default_content_setting_values.notifications" : 2}  #block notifications
    chrome_options.add_experimental_option("prefs",prefs)
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1050, 708)    
    driver.get(TARGET_URL1)
    u=WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="u"]')))
    u.send_keys(TARGET_URL)
    login_button=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="hide_register_save"]')))
    driver.implicitly_wait(10)
    login_button.click()
    driver.implicitly_wait(30)
    
    pyautogui.hotkey('ctrl', 's')
    time.sleep(1)
    pyautogui.typewrite(r'C:\Users\visha\Desktop\Harshit\Web site projects\Website Scrapper\page' + '.html')
    pyautogui.hotkey('enter')
