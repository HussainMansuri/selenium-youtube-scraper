from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import sys
import time
import pandas as pd
import mailer as ml
import config 
import datetime

# Set console encoding to UTF-8
sys.stdout.reconfigure(encoding='utf-8')
 


#Initializing Selenium Chrome Web Driver
def get_driver():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--headless')
    return webdriver.Chrome(options=chrome_options)



    driver.get(url)
    print('Page title: ', driver.title)


#Getting the list of the top trending videos
def get_videos(driver,url):
    driver.get(url)
    time.sleep(15)
    videos = driver.find_elements(By.TAG_NAME,'ytd-video-renderer')
    print(f"{len(videos)} fetched.")
    return videos


#Getting the title
def get_video_title(video): 
    title_tag = video.find_element(By.ID,'video-title')
    title = title_tag.text
    return title

#Getting the URL of the video
def get_url(video):
    title_tag = video.find_element(By.ID,'video-title')
    url = title_tag.get_attribute('href')
    return url
     


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
    uploaded_on = views_list[-1]
    return uploaded_on


#Getting the video description
def get_description(video):
    description_tag = video.find_element(By.ID,'description-text')
    desc = description_tag.text
    return desc


##Puting it all togather 

def parse_trending_videos(video):   
    #Getting the video title
    video_title = get_video_title(video)

    #Get video URL
    video_url = get_url(video)

    #Get channel name
    channel_name = get_channel_name(video)

    #Get channel url
    channel_url = get_channel_url(video)

    #Get view count
    views = get_views(video)

    #Getting uploaded on
    uploaded_on=get_uploaded_on(video)

    #Get video description
    desc = get_description(video)

    result_dict = {'video_title':video_title,
                    'video_url':video_url,
                    'channel_name':channel_name,
                    'channel_url':channel_url,
                    'views':views,
                    'uploaded':uploaded_on,
                    'description':desc
                    }
    return result_dict

   

if __name__ == "__main__":
    #Initializing the Selenium Chrome driver and getting the videos
    print("Initializing Chrome Driver...")
    youtube_treding_url = 'https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl'
    driver = get_driver()

    print("Fetching the trending videos....")
    videos = get_videos(driver,youtube_treding_url)

    #Parsing each video from the videos list and putting it in the result dictionary. 
    #parse_trending_videos() returns a dictionary with video information
    print("Parsing videos...")
    result=[parse_trending_videos(video) for video in videos]
    
    #Converting the list of dictionary into a Pandas dataframe
    print("All videos parsed!, creating DataFrame...")
    trending_df = pd.DataFrame(result,index=None)
    # print(trending_df)
    print(f"Dataframe {trending_df} created!")

    #Writing the datafram into a .csv file
    print("Writing Dataframe to .csv...")
    date_time = datetime.datetime.now()
    date_to_str = str(date_time).replace(' ','_').replace(':','_')
    filename = f'trending_videos_{date_to_str}.csv'
    trending_df.to_csv(filename,index=0)
    print(f'{filename} created!')

    #Sending file on email

    #importing secret variables 
    
    sender_email = config.email
    app_pass = config.app_pass
    reciever_email = config.reciever_email

    #email parameters
    from_name = 'Trendy Boi'
    to_name = 'Not so Trendy Boi'
    email_subject = 'Trendy youtube videos'
    email_body = f'''PFA, files with 'Top trending vidoes' on Youtube. Report pulled on {date_time}'''

    
    #calling the mailer function
    try:
        print("Sending email.....")
        ml.gmail_send_mail(to_name,from_name,email_subject,email_body,sender_email,app_pass,sender_email,reciever_email,file_name=filename)
    except:
        raise Exception("Program FAILED to send email, please check email parameters!!")
    else:
        print(f"Mail sent SUCCESSFULLY! to {reciever_email}")
    
    




