import requests
import pathlib
import json
from urllib.parse import unquote
from urllib.parse import urlsplit
from dotenv import load_dotenv
from process_image import download_image
from process_image import get_extension
import os


def get_nasa_pictures(directory_name,start_date, token):
    url = "https://api.nasa.gov/planetary/apod"
    payload = {
        "api_key":token,
        "start_date": start_date,
    }
    response = requests.get(url,params = payload)
    response.raise_for_status()
    all_photos = response.json()
    for i, one_photo in enumerate(all_photos):
        file_name = "nasa_apod{}{}".format(i,get_extension(one_photo["url"]))
        name_path = directory_name/ file_name
        download_image(one_photo["url"], name_path)
