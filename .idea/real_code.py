import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PROMISED_DOWN = 150
PROMISED_UP = 150
CHROME_DRIVER_PATH = Service("C:\Development\chromedriver.exe")
TWITTER_EMAIL = "ksashank129@gmail.com"
TWITTER_PASS = "twitter@1"


options  = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=CHROME_DRIVER_PATH,options=options)

driver.get("https://www.speedtest.net/")

start_test = driver.find_element(By.CLASS_NAME, "js-start-test")
time.sleep(3)

start_test.click()
time.sleep(60)
down_speed = driver.find_element(By.CLASS_NAME, "download-speed")

upload_speed = driver.find_element(By.CLASS_NAME, "upload-speed")

print(f"down : {down_speed.text}\nup: {upload_speed.text}")
time.sleep(5)
login = driver.get("https://twitter.com/i/flow/login")
time.sleep(5)
email = driver.find_element(By.TAG_NAME, "input")
email.send_keys(TWITTER_EMAIL)
email.send_keys(Keys.ENTER)
time.sleep(5)
usernsme = driver.find_element(By.TAG_NAME, "input")
usernsme.send_keys("kvsk129")
usernsme.send_keys(Keys.ENTER)
time.sleep(3)
password = driver.find_element(By.CSS_SELECTOR, ".r-homxoj")
password.send_keys(TWITTER_PASS)
password.send_keys(Keys.ENTER)
time.sleep(5)
tweet = driver.find_element(By.XPATH, "//a[@href='/compose/tweet']")
tweet.click()
time.sleep(2)
compose_t = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div")
compose_t.send_keys("j")
compose_t.send_keys(f"Hey Internet provider why is my speed {down_speed.text}down/{upload_speed.text}up when Iam paying for {PROMISED_DOWN}down/{PROMISED_UP}up")
tweet_click = driver.find_element(By.XPATH, "//*[text()='Tweet']")
tweet_click.click()