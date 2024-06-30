import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions
import csv
from selenium.webdriver.chrome.options import Options
from time import sleep
import chromedriver_autoinstaller
from selenium import webdriver
import datetime 

opt = webdriver.ChromeOptions()
opt.add_argument("--start-maximized")

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(options=opt)

def scroll_to_bottom(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

url = "https://www.jumia.com.tn/mlp-telephone-tablette/smartphones/" 
driver.get(url)

for _ in range(5): 
    scroll_to_bottom(driver)

listtitre = []
listprice = []
date_scrapy = datetime.datetime.now()

listdiv = driver.find_elements(By.XPATH, '//*[@id="jm"]/div/')
#listdiv = driver.find_elements(By.XPATH, '//*[@id="search-area"]/div[2]/div/div/div')
print(len(listdiv))

for div in listdiv:
    titre = div.find_element(By.XPATH, './/span[contains(@class, "ReactFlagsSelect-module_selectValue")]/span[contains(@class, "ReactFlagsSelect-module_label")] | .//span[contains(@class, "font-italic")] | .//div[contains(@class, "font-weight-bold") and contains(@class, "mb-0")]')
    price = div.find_element(By.XPATH, './/div[contains(@class, "h6") and contains(@class, "font-weight-bold") and contains(@class, "text-primary") and contains(@class, "mb-0")]')
    listtitre.append(titre.text)
    listprice.append(price.text)

# Add the date_scrapy to the information
data = list(zip(listtitre, listprice, [date_scrapy] * len(listtitre)))

print(data)