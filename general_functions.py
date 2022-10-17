import os.path
from urllib.parse import urlparse
import requests

def get_file_extension(url):
    url_parse = urlparse(url)
    extension = os.path.splitext(url_parse.path)[1]
    return extension


def download_image(url, path, params):
    response = requests.get(url, params=params)
    response.raise_for_status()

    with open(path, "wb") as f:
        f.write(response.content)



