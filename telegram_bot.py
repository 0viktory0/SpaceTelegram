import argparse
import os
import random
import time
from dotenv import load_dotenv
import telegram

def input_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seconds_delay", help="Задержка, сек", default="14400", type=int)
    parser.add_argument("--image_path", help="Выберете фотогафию или папку")
    args = parser.parse_args()
    return args


def send_image(path, token):
    bot = telegram.Bot(token=token)
    seconds = 5
    with open(path, "rb") as pictures:
        try:
            bot.send_photo(channel_id, pictures)
        except telegram.error.NetworkError:
            print("Не удалось подключиться к серверу. Проверьте подключение к интернету.")
            time.sleep(seconds)


def send_random_images(paths, token, seconds_delay):
    while True:
        random.shuffle(paths)
        for path in paths:
            send_image(path, token)
            time.sleep(seconds_delay)


def add_photo_paths():
    paths = list()
    for root, directory, filenames in os.walk("images"):
        for picture in filenames:
            paths.append(os.path.join(root, picture))
    return paths


if __name__ == "__main__":
    load_dotenv()
    channel_id = os.environ["CHANNEL_ID"]
    telegram_token = os.environ["TELEGRAM_TOKEN"]

    args = input_parse()
    path = args.image_path
    paths = add_photo_paths()
    seconds_delay = args.seconds_delay

 
    if args.image_path:
        send_image(path, telegram_token)
    else:
        send_random_images(paths, telegram_token, seconds_delay)
