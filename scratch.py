import requests

youtube_treding_url = 'https://www.youtube.com/feed/trending'

response = requests.get(youtube_treding_url)

# print(response.status_code)

# print('Output: ', response.text[:1000])

with open('trending.html','w') as f:
  f.write(response.text)
