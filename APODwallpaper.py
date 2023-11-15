import requests
import os

def get_APOD(filename):

    APOD_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

    response = requests.get(APOD_url)

    response_json = response.json()

    with open(filename, 'wb') as f:
        f.write(requests.get(response_json['hdurl']).content)

def clear_folder(filename):
    if os.path.exists(filename):
        os.remove(filename)

filepath = 'Wallpapers/APOD.png'

clear_folder(filepath)
get_APOD(filepath)