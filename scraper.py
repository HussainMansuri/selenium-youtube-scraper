from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import sys

# Set console encoding to UTF-8
sys.stdout.reconfigure(encoding='utf-8')

youtube_treding_url = 'https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl'
def get_driver():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--headless')
    return webdriver.Chrome(options=chrome_options)

if __name__ == "__main__":
    print("Getting driver")
    driver = get_driver()
    driver.get(youtube_treding_url)
    print('Page title: ', driver.title)

    print("Getting videos")
    videos = driver.find_elements(By.TAG_NAME,'ytd-video-renderer')
    print(f'Found {len(videos)} videos')

    print("Parsing the first video")
    #Title,url,tumbnail_url,channel,view,uploaded,description
    video =videos[0]

    #Getting the title
    title_tag = video.find_element(By.ID,'video-title')
    title = title_tag.text

    #Getting the URL
    url = title_tag.get_attribute('href')

    #Getting the thumbnail
    thumbnail_tag = video.find_element(By.ID,'thumbnail')
    thumbnail = thumbnail_tag.get_attribute('href')

    #Getting channel name
    channel_tag = video.find_element(By.CLASS_NAME,'yt-formatted-string')
    channel_name = channel_tag.text

    #Getting the channel url
    channel_url = channel_tag.get_attribute('href')

    #Getting the view count and upload
    views_tag = video.find_element(By.TAG_NAME,'ytd-video-meta-block')
    views = views_tag.find_element(By.CLASS_NAME,"ytd-video-meta-block")
    



    print("Title: ",title)
    print("URL: ",url)
    print("Thumbnail: ",thumbnail)
    print('Channel_name: ',channel_name)
    print('Channel_url: ',channel_url)
    print('Views: ',views)
    

     

    


