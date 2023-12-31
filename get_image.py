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
from dotenv  import load_dotenv

        
def create_parser ():
    parser = argparse.ArgumentParser(description='Программа предназначена для получения снимков')
    parser.add_argument('--id',default = "5eb87d47ffd86e000604b38a", help = "id одного из запусков SpaceX")
    return parser


if __name__ == '__main__':
    load_dotenv()
    token = os.environ["NASA_API_TOKEN"]
    folder_name = os.environ["IMAGE_NAME_FOLDER"]
    number_of_days = os.environ["NUMBER_DAYS"]
    start_date = os.environ["START_DATE"]
    
    path = pathlib.Path(folder_name)
    path.mkdir(parents=True, exist_ok=True)
    parser = create_parser()
    args = parser.parse_args()
    
    fetch_spacex_last_launch(args.id, path)
    
    get_nasa_pictures(path,start_date,token)

    get_epic(path,number_of_days,token)
