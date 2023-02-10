from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

options = Options()
options.set_preference("security.insecure_field_warning.contextual.enabled", False)
options.set_preference("security.insecure_password.ui.enabled", False)
options.set_preference("security.tls.version.min", 1)
options.set_preference("security.tls.version.max", 3)
options.set_preference("security.tls.version.fallback-limit", 3)
options.set_preference("browser.tabs.remote.autostart.2", False)
options.set_preference("browser.tabs.remote.autostart.1", False)

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
driver.get("<url do dashboard 1>")

driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get("<url do monitoramento 2>")

time.sleep(30)

while True:
	driver.switch_to.window(driver.window_handles[0])
	time.sleep(30)
	driver.switch_to.window(driver.window_handles[1])
	time.sleep(30)
