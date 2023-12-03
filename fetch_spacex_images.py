import requests
import pathlib
import os
from process_image import download_image
from process_image import get_extension

def fetch_spacex_last_launch(url, directory_name):
    response = requests.get(url)
    response.raise_for_status()
    image_urls = response.json()['links']['flickr']['original']
    for i, url in enumerate(image_urls):
        file_name = 'space_{}.jpeg'.format(i)
        output_name = directory_name / file_name
        download_image(url,output_name)
        
