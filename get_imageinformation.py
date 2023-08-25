import requests
import pathlib
import json
from urllib.parse import unquote
from urllib.parse import urlsplit
import os
import datetime
import argparse
from fetch_spacex_images import fetch_spacex_last_launch
from get_nasa_picture import get_nasa_pictures
from get_epic import get_epic
from dotenv import load_dotenv

today = datetime.date.today()

def get_extension(url):
    (scheme, netloc, path, query, fragment) = urlsplit(url)
    (head,tail) = os.path.split(unquote(path))
    (root,ext) = os.path.splitext(tail)
    return ext
    
    
def createParser ():
    parser = argparse.ArgumentParser(description='Программа предназначена для получения снимков SpaceX')
    parser.add_argument('--id',default = "5eb87d47ffd86e000604b38a")
    return parser

if __name__ == '__main__':
    load_dotenv()
    token = os.environ["API_TOKEN"]
    folder_name = os.environ["NAME_FOLDER"]
    number_of_days = os.environ["NUMBER_DAYS"]
    start_date = os.environ["START_DATE"]
    path = pathlib.Path(folder_name)
    path.mkdir(parents=True, exist_ok=True)
    parser = createParser()
    args = parser.parse_args()
    url_new = "https://api.spacexdata.com/v5/launches/{}".format(args.id)
    fetch_spacex_last_launch(url_new, path)
    url_nasa = "https://api.nasa.gov/planetary/apod"
    get_nasa_pictures(url_nasa,path,start_date,token)
    url_earth = "https://api.nasa.gov/EPIC/api/natural/date/"
    get_epic(url_earth,path,number_of_days,token)
