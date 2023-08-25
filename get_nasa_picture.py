import requests
import pathlib
import json
from urllib.parse import unquote
from urllib.parse import urlsplit
from dotenv import load_dotenv
import os

def download_image(url, name_path):
    headers = {
        'User-Agent': 'curl'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    with open(name_path, 'wb') as file:
        file.write(response.content)


def get_extension(url):
    (scheme, netloc, path, query, fragment) = urlsplit(url)
    (head,tail) = os.path.split(unquote(path))
    (root,ext) = os.path.splitext(tail)
    return ext


def get_nasa_pictures(url, name_directory,start_date, token):
    payload = {"api_key":token,
                "start_date": start_date
    }
    response = requests.get(url,params = payload)
    response.raise_for_status()
    all_dictionary = response.json()
    for i, daily_dictionary in enumerate(all_dictionary):
        print(daily_dictionary["url"])
        name_of_file = "nasa_apod{}".format(i)+get_extension(daily_dictionary["url"])
        name_path = name_directory/ name_of_file
        download_image(daily_dictionary["url"], name_path)
