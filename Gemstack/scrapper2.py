import webbrowser
from bs4 import BeautifulSoup, NavigableString, Tag 
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import  os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

chrome_options = Options()

prefs = {"profile.default_content_setting_values.notifications" : 2}  #block notifications

chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--load-extension=" + r"C:\Users\Hardik Airen\AppData\Local\Google\Chrome\User Data\Default\Extensions\ookhnhpkphagefgdiemllfajmkdkcaim\2.14.9_0") #<== loading unpacked extension
#chrome_options.add_argument("--headless")
#chrome_options.add_argument("--disable-setuid-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
#chrome_options.add_argument('--disable-

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://partner.engineer.ai/login")
driver.implicitly_wait(20)
driver.maximize_window()

user_name='/html/body/app/div/div[4]/main/login/div/div[2]/form/div/div/div/div[1]/input'
password='/html/body/app/div/div[4]/main/login/div/div[2]/form/div/div/div/div[2]/input'
submit_button='/html/body/app/div/div[4]/main/login/div/div[2]/form/div/div/div/button'
billing_button='/html/body/app/div/div[4]/main/core/div/left-menu/div/ul/li[3]'
no_thanks_button='//*[@id="onesignal-slidedown-cancel-button"]'
tracked_hours_section='/html/body/app/div/div[4]/main/core/div/div/div/billing/ul/li[3]'
#on_login_page
driver.find_element_by_xpath(user_name).send_keys('contact@gemstack.in')
driver.find_element_by_xpath(password).send_keys('contact.gemstack')
driver.find_element_by_xpath(submit_button).click()
#choosing billing from left menu
driver.implicitly_wait(20)
driver.find_element_by_xpath(billing_button).click()
