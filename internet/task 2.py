from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_driver_path = 'D:\\soft\\chromedriver\\chromedriver-win64\\chromedriver.exe'

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://github.com/vashpasha")

driver.add_cookie({"name": "myCookie", "value": "hello world"})

cookie = driver.get_cookie("myCookie")
print(f"cookie: {cookie['value']}")

driver.delete_cookie("myCookie")

cookie = driver.get_cookie("myCookie")
print(f"cookie: {cookie}")

driver.quit()
