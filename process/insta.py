from lib2to3.pgen2 import token
from msilib.schema import Directory
import requests
import os
import pathlib as Path
from utils.textgen import TextGen
from utils.hashget import HashFetcher
from utils.imageget import ImageGetter
import time 
import json
import schedule
import shutil

#Each postPicture is identical, the only difference is that each one targets a different photo on the webserver
#Updates will be made to shorten code and make it more effcient, but this works for now

def postPicture1():
    d = TextGen()
    f = HashFetcher()
    img_dir = "URL TO IMAGE"
    quote = d.get_textdata()
    hashtags = f.fetch()

    caption =  "{}~~~~~~~~~~~~~~~{}".format(quote, hashtags)

    time.sleep(5)
    token = "YOUR LONG-LIVED USER ACCESS TOKEN"
    post_url = "https://graph.facebook.com/v13.0/{}/media".format("YOUR INSTAGRAM USER ID")
    load_data = {
        "image_url": img_dir,
        "caption": caption,
        "access_token": token
    }
    r = requests.post(post_url, data=load_data)
    print(r.text)
    result = json.loads(r.text)
    if "id" in result:
        creation_id = result['id']

        second_post = "https://graph.facebook.com/v13.0/{}/media_publish".format("YOUR INSTAGRAM USER ID")
        second_data = {
            "creation_id": creation_id,
            "access_token": token
        }
        r = requests.post(second_post, data=second_data)
        print('Posted!')
        print(r.text)
    else:
        print("There was a problem")
def postPicture2():
    d = TextGen()
    f = HashFetcher()
    img_dir = "URL TO IMAGE"
    quote = d.get_textdata()
    hashtags = f.fetch()

    caption =  "{}~~~~~~~~~~~~~~~{}".format(quote, hashtags)

    time.sleep(5)
    token = "YOUR LONG-LIVED USER ACCESS TOKEN"
    post_url = "https://graph.facebook.com/v13.0/{}/media".format("YOUR INSTAGRAM USER ID")
    load_data = {
        "image_url": img_dir,
        "caption": caption,
        "access_token": token
    }
    r = requests.post(post_url, data=load_data)
    print(r.text)
    result = json.loads(r.text)
    if "id" in result:
        creation_id = result['id']

        second_post = "https://graph.facebook.com/v13.0/{}/media_publish".format("YOUR INSTAGRAM USER ID")
        second_data = {
            "creation_id": creation_id,
            "access_token": token
        }
        r = requests.post(second_post, data=second_data)
        print('Posted!')
        print(r.text)
    else:
        print("There was a problem")
def postPicture3():
    d = TextGen()
    f = HashFetcher()
    img_dir = "URL TO IMAGE"
    quote = d.get_textdata()
    hashtags = f.fetch()

    caption =  "{}~~~~~~~~~~~~~~~{}".format(quote, hashtags)

    time.sleep(5)
    token = "YOUR LONG-LIVED USER ACCESS TOKEN"
    post_url = "https://graph.facebook.com/v13.0/{}/media".format("YOUR INSTAGRAM USER ID")
    load_data = {
        "image_url": img_dir,
        "caption": caption,
        "access_token": token
    }
    r = requests.post(post_url, data=load_data)
    print(r.text)
    result = json.loads(r.text)
    if "id" in result:
        creation_id = result['id']

        second_post = "https://graph.facebook.com/v13.0/{}/media_publish".format("YOUR INSTAGRAM USER ID")
        second_data = {
            "creation_id": creation_id,
            "access_token": token
        }
        r = requests.post(second_post, data=second_data)
        print('Posted!')
        print(r.text)
    else:
        print("There was a problem")
def postPicture4():
    d = TextGen()
    f = HashFetcher()
    img_dir = "URL TO IMAGE"
    quote = d.get_textdata()
    hashtags = f.fetch()

    caption =  "{}~~~~~~~~~~~~~~~{}".format(quote, hashtags)

    time.sleep(5)
    token = "YOUR LONG-LIVED USER ACCESS TOKEN"
    post_url = "https://graph.facebook.com/v13.0/{}/media".format("YOUR INSTAGRAM USER ID")
    load_data = {
        "image_url": img_dir,
        "caption": caption,
        "access_token": token
    }
    r = requests.post(post_url, data=load_data)
    print(r.text)
    result = json.loads(r.text)
    if "id" in result:
        creation_id = result['id']

        second_post = "https://graph.facebook.com/v13.0/{}/media_publish".format("YOUR INSTAGRAM USER ID")
        second_data = {
            "creation_id": creation_id,
            "access_token": token
        }
        r = requests.post(second_post, data=second_data)
        print('Posted!')
        print(r.text)
    else:
        print("There was a problem") 
def postPicture5():
    d = TextGen()
    f = HashFetcher()
    img_dir = "URL TO IMAGE"
    quote = d.get_textdata()
    hashtags = f.fetch()

    caption =  "{}~~~~~~~~~~~~~~~{}".format(quote, hashtags)

    time.sleep(5)
    token = "YOUR LONG-LIVED USER ACCESS TOKEN"
    post_url = "https://graph.facebook.com/v13.0/{}/media".format("YOUR INSTAGRAM USER ID")
    load_data = {
        "image_url": img_dir,
        "caption": caption,
        "access_token": token
    }
    r = requests.post(post_url, data=load_data)
    print(r.text)
    result = json.loads(r.text)
    if "id" in result:
        creation_id = result['id']

        second_post = "https://graph.facebook.com/v13.0/{}/media_publish".format("YOUR INSTAGRAM USER ID")
        second_data = {
            "creation_id": creation_id,
            "access_token": token
        }
        r = requests.post(second_post, data=second_data)
        print('Posted!')
        print(r.text)
    else:
        print("There was a problem")
def postPicture6():
    d = TextGen()
    f = HashFetcher()
    img_dir = "URL TO IMAGE"
    quote = d.get_textdata()
    hashtags = f.fetch()

    caption =  "{}~~~~~~~~~~~~~~~{}".format(quote, hashtags)

    time.sleep(5)
    token = "YOUR LONG-LIVED USER ACCESS TOKEN"
    post_url = "https://graph.facebook.com/v13.0/{}/media".format("YOUR INSTAGRAM USER ID")
    load_data = {
        "image_url": img_dir,
        "caption": caption,
        "access_token": token
    }
    r = requests.post(post_url, data=load_data)
    print(r.text)
    result = json.loads(r.text)
    if "id" in result:
        creation_id = result['id']

        second_post = "https://graph.facebook.com/v13.0/{}/media_publish".format("YOUR INSTAGRAM USER ID")
        second_data = {
            "creation_id": creation_id,
            "access_token": token
        }
        r = requests.post(second_post, data=second_data)
        print('Posted!')
        print(r.text)
    else:
        print("There was a problem")
def postPicture7():
    d = TextGen()
    f = HashFetcher()
    img_dir = "URL TO IMAGE"
    quote = d.get_textdata()
    hashtags = f.fetch()

    caption =  "{}~~~~~~~~~~~~~~~{}".format(quote, hashtags)

    time.sleep(5)
    token = "YOUR LONG-LIVED USER ACCESS TOKEN"
    post_url = "https://graph.facebook.com/v13.0/{}/media".format("YOUR INSTAGRAM USER ID")
    load_data = {
        "image_url": img_dir,
        "caption": caption,
        "access_token": token
    }
    r = requests.post(post_url, data=load_data)
    print(r.text)
    result = json.loads(r.text)
    if "id" in result:
        creation_id = result['id']

        second_post = "https://graph.facebook.com/v13.0/{}/media_publish".format("YOUR INSTAGRAM USER ID")
        second_data = {
            "creation_id": creation_id,
            "access_token": token
        }
        r = requests.post(second_post, data=second_data)
        print('Posted!')
        print(r.text)
    else:
        print("There was a problem")
def postPicture8():
    d = TextGen()
    f = HashFetcher()
    img_dir = "URL TO IMAGE"
    quote = d.get_textdata()
    hashtags = f.fetch()

    caption =  "{}~~~~~~~~~~~~~~~{}".format(quote, hashtags)

    time.sleep(5)
    token = "YOUR LONG-LIVED USER ACCESS TOKEN"
    post_url = "https://graph.facebook.com/v13.0/{}/media".format("YOUR INSTAGRAM USER ID")
    load_data = {
        "image_url": img_dir,
        "caption": caption,
        "access_token": token
    }
    r = requests.post(post_url, data=load_data)
    print(r.text)
    result = json.loads(r.text)
    if "id" in result:
        creation_id = result['id']

        second_post = "https://graph.facebook.com/v13.0/{}/media_publish".format("YOUR INSTAGRAM USER ID")
        second_data = {
            "creation_id": creation_id,
            "access_token": token
        }
        r = requests.post(second_post, data=second_data)
        print('Posted!')
        print(r.text)
    else:
        print("There was a problem")
def postPicture9():
    d = TextGen()
    f = HashFetcher()
    img_dir = "URL TO IMAGE"
    quote = d.get_textdata()
    hashtags = f.fetch()

    caption =  "{}~~~~~~~~~~~~~~~{}".format(quote, hashtags)

    time.sleep(5)
    token = "YOUR LONG-LIVED USER ACCESS TOKEN"
    post_url = "https://graph.facebook.com/v13.0/{}/media".format("YOUR INSTAGRAM USER ID")
    load_data = {
        "image_url": img_dir,
        "caption": caption,
        "access_token": token
    }
    r = requests.post(post_url, data=load_data)
    print(r.text)
    result = json.loads(r.text)
    if "id" in result:
        creation_id = result['id']

        second_post = "https://graph.facebook.com/v13.0/{}/media_publish".format("YOUR INSTAGRAM USER ID")
        second_data = {
            "creation_id": creation_id,
            "access_token": token
        }
        r = requests.post(second_post, data=second_data)
        print('Posted!')
        print(r.text)
    else:
        print("There was a problem")
def postPicture10():
    d = TextGen()
    f = HashFetcher()
    img_dir = "URL TO IMAGE"
    quote = d.get_textdata()
    hashtags = f.fetch()

    caption =  "{}~~~~~~~~~~~~~~~{}".format(quote, hashtags)

    time.sleep(5)
    token = "YOUR LONG-LIVED USER ACCESS TOKEN"
    post_url = "https://graph.facebook.com/v13.0/{}/media".format("YOUR INSTAGRAM USER ID")
    load_data = {
        "image_url": img_dir,
        "caption": caption,
        "access_token": token
    }
    r = requests.post(post_url, data=load_data)
    print(r.text)
    result = json.loads(r.text)
    if "id" in result:
        creation_id = result['id']

        second_post = "https://graph.facebook.com/v13.0/{}/media_publish".format("YOUR INSTAGRAM USER ID")
        second_data = {
            "creation_id": creation_id,
            "access_token": token
        }
        r = requests.post(second_post, data=second_data)
        print('Posted!')
        print(r.text)
        resetMediaPOST(done_with_post=True)
    else:
        print("There was a problem")
        resetMediaPOST(done_with_post=True)


# This function is triggers after postPicture10() is executed
#The webserver is sole designed to handle GET/POST/DELETE Methods
#Code for websever will be uploaded soon for "security" purposes :)
def resetMediaPOST(done_with_post):
    if done_with_post is True:
        mediaserver_url = "URL TO WEBSERVER WITH IMAGES"
        #Will delete everything from webservers media folder
        r = requests.delete(mediaserver_url)
        print(r.text)

        print("Waiting 2 minutes until post")

        time.sleep(120)
        #After webserver is done deleting all photos, I also deletes the local photos 
        folder = "instabot\\process\\utils\\content"
        folderdirlist = os.listdir(folder)
        for filename in folderdirlist:
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))
        g = ImageGetter()
        #Loads 10 new images in content folder
        g.retrieve_imgs()

        time.sleep(120)

        i = {}
        #Will send a post request and send each one of the new photos to the webserver media folder 
        for i in folderdirlist:
            files = {"file" : open("C:/Users/fguin/OneDrive/Desktop/instabot/process/utils/content/{}".format(i),"rb")}
            l = requests.post(mediaserver_url, files=files)
        print(l.text)
        done_with_post = False
    return done_with_post

#Will Schedule to do each job at a specified time
schedule.every().day.at("12:30:00").do(postPicture1)
schedule.every().day.at("13:30:00").do(postPicture2)
schedule.every().day.at("14:30:00").do(postPicture3)
schedule.every().day.at("15:30:00").do(postPicture4)
schedule.every().day.at("18:30:00").do(postPicture5)
schedule.every().day.at("21:30:00").do(postPicture6)
schedule.every().day.at("00:30:00").do(postPicture7)
schedule.every().day.at("03:30:00").do(postPicture8)
schedule.every().day.at("06:30:00").do(postPicture9)
schedule.every().day.at("10:30:00").do(postPicture10)


while True:
    schedule.run_pending()
    time.sleep(1)



