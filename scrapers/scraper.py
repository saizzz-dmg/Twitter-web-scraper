from datetime import datetime
import time , random
from selenium import webdriver
from selenium.webdriver import ChromeOptions, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# import random

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


    # proxy = random.choice(ip_addresses)
    # options.add_argument(f'--proxy-server={proxy}')

    options.add_argument("--start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("detach" , True)

    driver = webdriver.Chrome(options=options)
    url = "https://twitter.com/i/flow/login"
    driver.get(url)

    username = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[autocomplete="username"]')))
    username.send_keys("<email>")
    username.send_keys(Keys.ENTER)
    username = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[autocomplete="on"]')))
    username.send_keys("<username")
    username.send_keys(Keys.ENTER)
    password = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="password"]')))
    password.send_keys("<password>")
    password.send_keys(Keys.ENTER)
    show_more = WebDriverWait(driver , 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR ,'a[href="/explore/tabs/for-you"]')))
    show_more.click()
    contents_whats_happening = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[aria-label="Timeline: Explore"]')))
    titles = contents_whats_happening.find_elements(By.CLASS_NAME ,"r-1bymd8e")
# <a href="/explore/tabs/for-you" role="link" class="css-175oi2r r-w7s2jr r-3pj75a r-o7ynqc r-6416eg r-1ny4l3l r-1loqt21"><div dir="ltr" class="css-146c3p1 r-bcqeeo r-1ttztb7 r-qvutc0 r-37j5jr r-a023e6 r-rjixqe r-16dba41" style="text-overflow: unset; color: rgb(29, 155, 240);"><span class="css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3" style="text-overflow: unset;">Show more</span></div></a>

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

    contents_whats_happening = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[aria-label="Timeline: Explore"]')))
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








