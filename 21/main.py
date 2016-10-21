import urllib.request
import random

def download_image_url(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)

download_image_url("https://i.stack.imgur.com/irPvV.png?s=32&g=1")