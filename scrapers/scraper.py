from datetime import datetime
import time , random
from selenium import webdriver
from selenium.webdriver import ChromeOptions, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

ip_addresses = [
    "192.168.1.1",
    "10.0.0.1",
    "172.16.254.1",
    "8.8.8.8",
    "203.0.113.5",
    "192.0.2.1",
    "198.51.100.2",
    "192.88.99.1",
    "198.18.0.1",
    "192.31.196.1"
]


driver = ''
def scraper_func():
    global driver 
    ini_dict = dict()

    options = ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("detach" , True)

    driver = webdriver.Chrome(options=options)
    url = "https://twitter.com/i/flow/login"
    driver.get(url)

    username = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[autocomplete="username"]')))
    username.send_keys("n85442525@gmail.com")
    username.send_keys(Keys.ENTER)
    username = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[autocomplete="on"]')))
    username.send_keys("newuser2110132")
    username.send_keys(Keys.ENTER)
    password = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="password"]')))
    password.send_keys("randompassword123")
    password.send_keys(Keys.ENTER)
    contents_whats_happening = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[aria-label="Timeline: Trending now"]')))
    titles = contents_whats_happening.find_elements(By.CLASS_NAME ,"r-1bymd8e")


    for i , title in enumerate(titles[0:5]):
        ini_dict[f'nameoftrend{i+1}'] = title.text


    current_time_date = datetime.now()
    formatted_time = current_time_date.strftime("%H:%M:%S")
    formatted_date = current_time_date.strftime("%d-%m-%Y")
    ini_dict['dateofcreation'] = formatted_date
    ini_dict['timeofcreation'] = formatted_time
    ini_dict['ip']= random.choice(ip_addresses)

    return ini_dict

def refresh_scraper_func():
    ini_dict = dict()

    driver.refresh()

    contents_whats_happening = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[aria-label="Timeline: Trending now"]')))
    titles = contents_whats_happening.find_elements(By.CLASS_NAME , "r-1bymd8e")


    for i , title in enumerate(titles[0:5]):
        ini_dict[f'nameoftrend{i+1}'] = title.text


    current_time_date = datetime.now()
    formatted_time = current_time_date.strftime("%H:%M:%S")
    formatted_date = current_time_date.strftime("%d-%m-%Y")
    ini_dict['dateofcreation'] = formatted_date
    ini_dict['timeofcreation'] = formatted_time
    ini_dict['ip']= random.choice(ip_addresses)


    return ini_dict








