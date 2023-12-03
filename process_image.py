import requests
import pathlib
import json
from urllib.parse import unquote
from urllib.parse import urlsplit
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
    scheme, netloc, path, query, fragment = urlsplit(url)
    head,tail = os.path.split(unquote(path))
    root,ext = os.path.splitext(tail)
    return ext
