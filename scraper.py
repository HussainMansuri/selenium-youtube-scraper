from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import sys

# Set console encoding to UTF-8
sys.stdout.reconfigure(encoding='utf-8')

youtube_treding_url = 'https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl'

#Initializing Selenium Chrome Web Driver
def get_driver():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--headless')
    return webdriver.Chrome(options=chrome_options)


#Getting the title of the Webpage
def get_title(driver):
    driver.get(youtube_treding_url)
    print('Page title: ', driver.title)


#Getting the list of the top trending videos
def get_videos(driver):
    print("Getting videos")
    videos = driver.find_elements(By.TAG_NAME,'ytd-video-renderer')
    print(f"{len(videos)} fetched.")
    return videos


#Getting the title
def get_title(video): 
    title_tag = video.find_element(By.ID,'video-title')
    title = title_tag.text
    return title

#Getting the URL of the video
def get_url(video):
    title_tag = video.find_element(By.ID,'video-title')
    url = title_tag.get_attribute('href')
    return url
     
#Getting the video thumbnail
def get_thumbnail(video):
    thumbnail_tag = video.find_element(By.ID,'thumbnail')
    thumbnail = thumbnail_tag.get_attribute('href')
    return thumbnail

#Getting the channel name
def get_channel_name(video):
    channel_tag = video.find_element(By.CLASS_NAME,'yt-formatted-string')
    channel_name = channel_tag.text
    return channel_name

#Getting the channel_url
def get_channel_url(video):
    channel_tag = video.find_element(By.CLASS_NAME,'yt-formatted-string')
    channel_url = channel_tag.get_attribute('href')
    return channel_url
     
     
#Getting the view count and uploaded on:
def get_views(video):
    views_tag = video.find_element(By.TAG_NAME,'ytd-video-meta-block')
    views_list = []
    views_list = views_tag.find_element(By.CLASS_NAME,"ytd-video-meta-block").text.split('\n')
    views = views_list[-2]
    return views

#Get uploaded on
def get_uploaded_on(video):
    views_tag = video.find_element(By.TAG_NAME,'ytd-video-meta-block')
    views_list = []
    views_list = views_tag.find_element(By.CLASS_NAME,"ytd-video-meta-block").text.split('\n')
    views = views_list[-2]
    uploaded_on = views[-1]
    return views


#Getting the video description
def get_description(video):
    description_tag = video.find_element(By.ID,'description-text')
    desc = description_tag.text
    return desc





if __name__ == "__main__":
    # print("Getting driver")
    # driver = get_driver()
    # driver.get(youtube_treding_url)
    

    # print("Getting videos")
    # videos = driver.find_elements(By.TAG_NAME,'ytd-video-renderer')
    # print(f'Found {len(videos)} videos')

    # print("Parsing the first video")
    # #Title,url,tumbnail_url,channel,view,uploaded,description
    # video =videos[0]

    # #Getting the title
    # title_tag = video.find_element(By.ID,'video-title')
    # title = title_tag.text

    # #Getting the URL
    # url = title_tag.get_attribute('href')

    # #Getting the thumbnail
    # thumbnail_tag = video.find_element(By.ID,'thumbnail')
    # thumbnail = thumbnail_tag.get_attribute('href')

    # #Getting channel name
    # channel_tag = video.find_element(By.CLASS_NAME,'yt-formatted-string')
    # channel_name = channel_tag.text

    # #Getting the channel url
    # channel_url = channel_tag.get_attribute('href')

    # #Getting the view count and upload
    # views_tag = video.find_element(By.TAG_NAME,'ytd-video-meta-block')
    # views_list = []
    # views_list = views_tag.find_element(By.CLASS_NAME,"ytd-video-meta-block").text.split('\n')
    # views = views_list[-2]
    # uploaded_on = views_list[-1]

    
    
    # #Getting the description
    # description_tag = video.find_element(By.ID,'description-text')
    # desc = description_tag.text




    # print("Title: ",title)
    # print("URL: ",url)
    # print("Thumbnail: ",thumbnail)
    # print('Channel_name: ',channel_name)
    # print('Channel_url: ',channel_url)
    # print('Views: ',views)
    # print('Uploaded: ',uploaded_on)
    # print("Description: ",desc)

     

    


