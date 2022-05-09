from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("start-maximized")
chrome_drive_path = "C:\Development\chromedriver.exe"
ser = Service(chrome_drive_path)
driver = webdriver.Chrome(service=ser, options=options)
driver.get("https://www.python.org/")

time = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

events = {}

for n in range(len(time)):
    events[n] = {
        "time" : time[n].text,
        "name" : event[n].text,
    }
print(events)
driver.quit()