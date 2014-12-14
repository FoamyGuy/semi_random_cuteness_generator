
# semi random cuteness generator
# pulls redit.com/r/aww returns a random png or jpeg from the front page.


from flask import Flask, redirect
import json, requests
import random
import os.path, time

app = Flask(__name__)

def is_data_current():
    last_modified = os.path.getmtime("./aww_posts.json")
    print (last_modified)
    now = time.time()
    print (now)
    one_hour = 60 * 60
    print (now - last_modified)
    if last_modified + one_hour > now:
        return True
    else:
        return False
        
def get_data():
    url = 'http://www.reddit.com/r/aww.json'
    resp = requests.get(url=url)
    print (resp.text)
    if "error" not in resp.text:
        f = open("./aww_posts.json", 'w')
        f.write(resp.text)
        f.close()
        
def get_links():
    print("data is %s." % is_data_current())
    if not is_data_current():
        print("data is old downloading.")
        get_data()
    f = open("aww_posts.json", 'r') 
    data = json.loads(f.read())
    f.close()
    
    raw_image_links = []
    for post in data['data']['children']:
        ending = post['data']['url'][-4:]
        if ending.lower() == ".jpg" or ending.lower() == ".png":
            raw_image_links.append(post['data']['url'])

    return raw_image_links



    
@app.route('/')
def hello_world():
    links = get_links()
    print (links)
    return redirect(random.choice(links), code=302)

"""
if __name__ == '__main__':
    app.run(debug=True)
"""    