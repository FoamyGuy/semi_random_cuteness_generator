
# semi random cuteness generator
# pulls redit.com/r/aww returns a random png or jpeg from the front page.

from flask import Flask, redirect
import json, requests
import random


app = Flask(__name__)

def get_links():
    url = 'http://www.reddit.com/r/aww.json'
    resp = requests.get(url=url)
    data = json.loads(resp.text)
    raw_image_links = []

    for post in data['data']['children']:
        ending = post['data']['url'][-4:]
        if ending.lower() == ".jpg" or ending.lower() == ".png":
            raw_image_links.append(post['data']['url'])

    return raw_image_links

app = Flask(__name__)


@app.route('/')
def hello_world():
    links = get_links()
    print (links)
    return redirect(random.choice(links), code=302)
