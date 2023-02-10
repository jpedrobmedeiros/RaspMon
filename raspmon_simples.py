from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pyautogui as pg
import time

options = Options()
options.set_preference("security.insecure_field_warning.contextual.enabled", False)
options.set_preference("security.insecure_password.ui.enabled", False)
options.set_preference("security.tls.version.min", 1)
options.set_preference("security.tls.version.max", 3)
options.set_preference("security.tls.version.fallback-limit", 3)

driver = webdriver.Firefox(options=options)
driver.fullscreen_window()

driver.get("<url do monitoramento 1>")

element = driver.find_element("xpath", '/html/body/div/div[1]/main/div[3]/div/div[2]/div/div/form/div[1]/div[2]/div[1]/div/input')
element.send_keys("<username>")
element = driver.find_element("xpath", '//*[@id="current-password"]')
element.send_keys("<password>")
element = driver.find_element("xpath", '/html/body/div/div[1]/main/div[3]/div/div[2]/div/div/form/button')
element.submit()

time.sleep(3)
driver.get("<url do dashboard>")
while True:
	time.sleep(3)
