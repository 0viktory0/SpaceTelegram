import requests
import os
import argparse
from general_functions import get_file_extension, download_image
from urllib.parse import urlparse

def fetch_spacex_photos(directory, launch_id):
    response = requests.get(f"https://api.spacexdata.com/v5/launches/{launch_id}")
    response.raise_for_status()
    image_url = response.json()["links"]["flickr"]["original"]

    for i, image in enumerate(image_url):
        download_image(image, os.path.join(directory, f"spacex{i}{get_file_extension(image)}"), params=None)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("launch_id", help="ID запуска", type=str, default="latest")
    launch_id = parser.parse_args().launch_id
    os.makedirs("images", exist_ok=True)

    fetch_spacex_photos("images", launch_id)

