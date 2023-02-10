from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

options = Options()
options.set_preference("security.insecure_field_warning.contextual.enabled", False)
options.set_preference("security.insecure_password.ui.enabled", False)
options.set_preference("security.tls.version.min", 1)
options.set_preference("security.tls.version.max", 3)
options.set_preference("security.tls.version.fallback-limit", 3)
options.set_preference("layout.css.devPixelsPerPx", "1.75")

driver = webdriver.Firefox(options=options)

screen_width = driver.execute_script("return screen.width")

driver.set_window_position(-screen_width, 0)
driver.fullscreen_window()

driver.get("<url do monitoramento>")

element = driver.find_element("xpath", '//*[@id="username"]')
element.send_keys("<username>")
element = driver.find_element("xpath", '//*[@id="password"]')
element.send_keys("<password>")
element = driver.find_element("xpath", '//*[@id="login"]')
element.submit()

time.sleep(3)

while True:
        time.sleep(30)
