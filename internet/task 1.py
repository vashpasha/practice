from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_driver_path = 'D:\\soft\\chromedriver\\chromedriver-win64\\chromedriver.exe'

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://github.com/vashpasha")

driver.execute_script("window.localStorage.setItem('myKey', 'hello world!');")

value = driver.execute_script("return window.localStorage.getItem('myKey');")
print(f"local storage value: {value}")

driver.execute_script("window.localStorage.removeItem('myKey');")

value = driver.execute_script("return window.localStorage.getItem('myKey');")
print(f"local storage value: {value}")

driver.quit()