import requests
import pathlib
import json
from urllib.parse import unquote
from urllib.parse import urlsplit
from process_image import get_extension
import os
import datetime


def get_epic(path, number_of_days,token):
    url = "https://api.nasa.gov/EPIC/api/natural/date/"
    dates = []
    for i in range(int(number_of_days)):
        date = datetime.date.today() - datetime.timedelta(days=i)
        formatted_date = date.strftime("%Y-%m-%d")
        dates.append(formatted_date)
    payload = {"api_key":token}
    for date in dates:
        url_earth = "{}{}".format(url,date)
        response = requests.get(url_earth,params = payload)
        response.raise_for_status()
        for one_photo in response.json():
            full_name = "https://api.nasa.gov/EPIC/archive/natural/{}/{}/{}/png/{}.png".format(one_photo['identifier'][0:4],one_photo['identifier'][4:6],one_photo['identifier'][6:8],one_photo['image'])
            file_name = "EPIC_{}{}".format(one_photo['identifier'],get_extension(full_name))
            name_path = path/ file_name
            epic_response = requests.get(full_name,params = payload)
            epic_response.raise_for_status()
            with open(name_path, 'wb') as file:
                file.write(epic_response.content)
