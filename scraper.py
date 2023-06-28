from selenium import webdriver

youtube_treding_url = 'https://www.youtube.com/feed/trending'

# driver = webdriver.Chrome('/full_path_to_chrome_driver')
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(options=chrome_options)

driver.get(youtube_treding_url)

print('Page title: ', driver.title)