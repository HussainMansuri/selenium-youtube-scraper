from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import sys
import time
import pandas as pd
import mailer as ml
import config 
import datetime

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--headless')
    return webdriver.Chrome(options=chrome_options)


def get_videos(driver,url):
    driver.get(url)
    time.sleep(15)
    videos = driver.find_elements(By.TAG_NAME,'ytd-video-renderer')
    print(f"{len(videos)} fetched.")
    return videos

def get_thumbnail(driver):
    driver.get('https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl')
    time.sleep(30)
    for i in driver.find_elements(By.CLASS_NAME,'yt-core-image--fill-parent-height.yt-core-image--fill-parent-width.yt-core-image.yt-core-image--content-mode-scale-aspect-fill.yt-core-image--loaded'):
        print(i.get_attribute('src'))

driver = get_driver()

get_thumbnail(driver)

