import requests
import os
from general_functions import get_file_extension, download_image
from dotenv import load_dotenv
import argparse
from urllib.parse import urlparse
import urllib.parse


def fetch_nasa_epic(token, directory):
    payload = {"api_key": token}
    response = requests.get("https://api.nasa.gov/EPIC/api/natural/images", params=payload)
    response.raise_for_status()
    epic_imgages = response.json()

    for num, image in enumerate(epic_imgages[:10]):
        image_name = image["image"]
        image_date = image["date"][:10].replace("-", "/")
        image_url = "https://api.nasa.gov/EPIC/" \
                    f"archive/natural/{image_date}" \
                    f"/png/{image_name}.png"
        payload = {"api_key": token}
        download_image(image_url, os.path.join(directory, f"nasa_space{num}{get_file_extension(image_url)}"), params=payload)


if __name__ == "__main__":
    load_dotenv()
    nasa_token = os.getenv("NASA_TOKEN")
    os.makedirs("images", exist_ok=True)

    fetch_nasa_epic(nasa_token, "images")