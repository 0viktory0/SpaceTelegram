import requests
import os
from general_functions import get_file_extension, download_image
from dotenv import load_dotenv
import argparse


def fetch_nasa_apod(token, directory):
    apod_url = f"https://api.nasa.gov/planetary/apod"
    payload = {"count": 30, "api_key": token}
    response = requests.get(apod_url, params=payload)
    response.raise_for_status()
    apod_imgages = response.json()

    for num, image_url in enumerate(apod_imgages):
        image_url = apod_imgages[num]["url"]
        download_image(image_url, os.path.join(directory, f"nasa_space{num}{get_file_extension(image_url)}"), params=None)


if __name__ == "__main__":
    load_dotenv()
    nasa_token = os.getenv("NASA_TOKEN")
    os.makedirs("images", exist_ok=True)

    fetch_nasa_apod(nasa_token, "images")