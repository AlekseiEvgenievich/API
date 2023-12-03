import requests
import pathlib
import json
from urllib.parse import unquote
from urllib.parse import urlsplit
from process_image import download_image
from process_image import get_extension
import os
import datetime


def get_epic(url, path, number_of_days,token):
    dates = [str(datetime.date.today() - datetime.timedelta(days=i)).split(" ")[0] for i in range(int(number_of_days))]
    payload = {"api_key":token}
    for date in dates:
        url_earth = "{}{}".format(url,date)
        response = requests.get(url_earth,params = payload)
        response.raise_for_status()
        for one_photo in response.json():
            full_name = "https://api.nasa.gov/EPIC/archive/natural/{}/{}/{}/png/{}.png?api_key={}".format(one_photo['identifier'][0:4],one_photo['identifier'][4:6],one_photo['identifier'][6:8],one_photo['image'],payload["api_key"])
            name_of_file = "EPIC_{}{}".format(one_photo['identifier'],get_extension(full_name))
            name_path = path/ name_of_file
            download_image(full_name,name_path)
