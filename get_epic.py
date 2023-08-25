import requests
import pathlib
import json
from urllib.parse import unquote
from urllib.parse import urlsplit
import os
import datetime


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


def get_epic(url, path, number_of_days,token):
    dates = [str(datetime.date.today() - datetime.timedelta(days=i)).split(" ")[0] for i in range(int(number_of_days))]
    payload = {"api_key":token}
    for date in dates:
        url_earth = url+date
        response = requests.get(url_earth,params = payload)
        response.raise_for_status()
        for one_response in response.json():
            full_name = "https://api.nasa.gov/EPIC/archive/natural/{}/{}/{}/png/{}.png?api_key={}".format(one_response['identifier'][0:4],one_response['identifier'][4:6],one_response['identifier'][6:8],one_response['image'],payload["api_key"])
            name_of_file = "EPIC_{}".format(one_response['identifier'])+get_extension(full_name)
            print(name_of_file)
            name_path = path/ name_of_file
            download_image(full_name,name_path)
