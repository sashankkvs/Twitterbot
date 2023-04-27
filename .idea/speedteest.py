import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PROMISED_DOWN = 150
PROMISED_UP = 150
CHROME_DRIVER_PATH = Service("C:\Development\chromedriver.exe")
options  = webdriver.ChromeOptions()
TWITTER_EMAIL = "ksashank129@gmail.com"
TWITTER_PASS = "twitter@1"


class Internetservicetweetbot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=CHROME_DRIVER_PATH,options=options)
        self.upload_speed = 0
        self.down_speed = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        start_test = self.driver.find_element(By.CLASS_NAME, "js-start-test")
        time.sleep(3)
        start_test.click()
        time.sleep(60)
        self.down_speed = self.driver.find_element(By.CLASS_NAME, "download-speed").text

        self.upload_speed = self.driver.find_element(By.CLASS_NAME, "upload-speed").text
        print(f"down : {self.down_speed}\nup: {self.upload_speed}")

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(5)
        email = self.driver.find_element(By.TAG_NAME, "input")
        email.send_keys(TWITTER_EMAIL)
        email.send_keys(Keys.ENTER)
        time.sleep(5)
        usernsme = self.driver.find_element(By.TAG_NAME, "input")
        usernsme.send_keys("kvsk129")
        usernsme.send_keys(Keys.ENTER)
        time.sleep(3)
        password = self.driver.find_element(By.CSS_SELECTOR, ".r-homxoj")
        password.send_keys(TWITTER_PASS)
        password.send_keys(Keys.ENTER)
        time.sleep(5)
        tweet = self.driver.find_element(By.XPATH, "//a[@href='/compose/tweet']")
        tweet.click()
        time.sleep(2)
        compose_t = self.driver.find_element(By.XPATH,
                                        "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div")
        compose_t.send_keys(
            f"Hey Internet provider why is my speed {self.down_speed}down/{self.upload_speed}up when Iam paying for {PROMISED_DOWN}down/{PROMISED_UP}up")
        tweet_click = self.driver.find_element(By.XPATH, "//*[text()='Tweet']")
        tweet_click.click()