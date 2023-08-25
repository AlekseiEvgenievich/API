import requests
import pathlib
import json
from urllib.parse import unquote
from urllib.parse import urlsplit
import os
import datetime
today = datetime.date.today()

# Subtract 30 days to get the starting date
#ll = str(today - datetime.timedelta(days=30)).split(" ")[0]
dates = [str(today - datetime.timedelta(days=i)).split(" ")[0] for i in range(30)]
print(dates)
def download_image(url, name_path):
    headers = {
        'User-Agent': 'curl'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    with open(name_path, 'wb') as file:
        file.write(response.content)
        
def fetch_spacex_last_launch(url, name_directory):
    response = requests.get(url)
    response.raise_for_status()
    image_urls = response.json()['links']['flickr']['original']
    for i, url in enumerate(image_urls):
        name_of_file = 'space_{}'.format(i) + '.jpeg'
        filename = name_directory / name_of_file
        download_image(url,filename)

def get_extension(url):
    (scheme, netloc, path, query, fragment) = urlsplit(url)
    (head,tail) = os.path.split(unquote(path))
    (root,ext) = os.path.splitext(tail)
    return ext

def get_nasa_picture(url, name_directory):
    payload = {"api_key":"3bK6nQQh2spBwLGJSAxakzWEwyM3bh7J5bEjDYa6",
                "start_date":"2023-07-24"
    }
    response = requests.get(url,params = payload)
    response.raise_for_status()
    all_dictionary = response.json()
    for i, daily_dictionary in enumerate(all_dictionary):
        print(daily_dictionary["url"])
        name_of_file = "nasa_apod{}".format(i)+get_extension(daily_dictionary["url"])
        name_path = name_directory/ name_of_file
        print(name_path)
        download_image(daily_dictionary["url"], name_path)

path = pathlib.Path('images')
path.mkdir(parents=True, exist_ok=True)
filename = path / 'hubble.jpeg'
url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
#download_image(url,filename)

url_new = "https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a"
#fetch_spacex_last_launch(url_new, path)
img_name = "https://example.com/txt/hello%20world.txt?v=9#python"
img_name1 = "http://example.com/image.png?v=9341124"
#print(get_extension(img_name1))

'''url_nasa = "https://api.nasa.gov/planetary/apod" '''
for i in range(0):
    current_date = str(today - datetime.timedelta(days=i)).split(" ")[0]
    print(current_date)
    url_earth = "https://api.nasa.gov/EPIC/api/natural/date/"+current_date
    payload = {"api_key":"3bK6nQQh2spBwLGJSAxakzWEwyM3bh7J5bEjDYa6"}
    response = requests.get(url_earth,params = payload)
    response.raise_for_status()
    for k in response.json():
        print("hui")
        print(k['identifier'][4:6])
        print(k['image'])
        full_name = "https://api.nasa.gov/EPIC/archive/natural/{}/{}/{}/png/{}.png?api_key={}".format(k['identifier'][0:4],k['identifier'][4:6],k['identifier'][6:8],k['image'],payload["api_key"])
        name_of_file = "EPIC_{}".format()+get_extension(full_name)
        name_path = path/ name_of_file
        #print(name_path)
        download_image(full_name,name_path)
#print(response.json())
#print(response.json()[0]['title'])
#print("Hello World!")
#get_nasa_picture(url_nasa,path)
#print(get_nasa_picture(url_nasa,path))
#for url in urls:
#    print(url["url"])

