import requests
import pathlib
import os

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
        
