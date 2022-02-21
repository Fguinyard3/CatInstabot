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

clientID = 1014072242527987
clientSECRET = "e767b3acdcd195641f0d9d90b5fa278a"



def get_TOKEN():
    url = "https://graph.facebook.com/v13.0/oauth/access_token?grant_type=fb_exchange_token&client_id=1014072242527987&client_secret=e767b3acdcd195641f0d9d90b5fa278a&fb_exchange_token=EAAOaSxfK3vMBAAEHkXVk5qvDh2ecSCjhb3OIoeLbFPs0EUhJNKtOEMNgGuXqtOWnSf43jqs3OaVczIsqgHAws6jZB11AEtZCIkD5bZAdvydERDn6oPjsyxgFDZAjKCuRdqLlGypJCgqVWbc1ZAHtAyXY2yrdPTmfiSNuzAM5cRFZCXgChXGPHjJYPLZB8Er6KZC5jGGEdOxs232gOU9GOPSLgXODnZBfp9Vywx1anEZCzUjjs5IKoKqlOJ"
    r = requests.post(url)
    print(r.text)
def postPicture1():
    d = TextGen()
    f = HashFetcher()
    img_dir = "http://34.73.246.95:8000/media/cat_image1.jpg"
    quote = d.get_textdata()
    hashtags = f.fetch()

    caption =  "{}~~~~~~~~~~~~~~~{}".format(quote, hashtags)

    time.sleep(5)
    token = "EAAOaSxfK3vMBAFjLvt5FsriZAoHXJLX4do5eRqJW0mdmzGcmlnFvqD8bffGR7M3Ov7jUTXVFc3YzPrSP4xccr6CdNZBTTrIQfwkpDW7L5zZClYknF8f1kLdN2kwqLUzRS2XMvgXdWx2ZBZAqZCxqm5axXT6iHQLS2aZC0zv0XGTeQZDZD"
    post_url = "https://graph.facebook.com/v13.0/{}/media".format("17841450326370751")
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

        second_post = "https://graph.facebook.com/v13.0/{}/media_publish".format("17841450326370751")
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
    img_dir = "http://34.73.246.95:8000/media/cat_image2.jpg"
    quote = d.get_textdata()
    hashtags = f.fetch()

    caption =  "{}~~~~~~~~~~~~~~~{}".format(quote, hashtags)

    time.sleep(5)
    token = "EAAOaSxfK3vMBAFjLvt5FsriZAoHXJLX4do5eRqJW0mdmzGcmlnFvqD8bffGR7M3Ov7jUTXVFc3YzPrSP4xccr6CdNZBTTrIQfwkpDW7L5zZClYknF8f1kLdN2kwqLUzRS2XMvgXdWx2ZBZAqZCxqm5axXT6iHQLS2aZC0zv0XGTeQZDZD"
    post_url = "https://graph.facebook.com/v13.0/{}/media".format("17841450326370751")
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

        second_post = "https://graph.facebook.com/v13.0/{}/media_publish".format("17841450326370751")
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
    img_dir = "http://34.73.246.95:8000/media/cat_image3.jpg"
    quote = d.get_textdata()
    hashtags = f.fetch()

    caption =  "{}~~~~~~~~~~~~~~~{}".format(quote, hashtags)

    time.sleep(5)
    token = "EAAOaSxfK3vMBAFjLvt5FsriZAoHXJLX4do5eRqJW0mdmzGcmlnFvqD8bffGR7M3Ov7jUTXVFc3YzPrSP4xccr6CdNZBTTrIQfwkpDW7L5zZClYknF8f1kLdN2kwqLUzRS2XMvgXdWx2ZBZAqZCxqm5axXT6iHQLS2aZC0zv0XGTeQZDZD"
    post_url = "https://graph.facebook.com/v13.0/{}/media".format("17841450326370751")
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

        second_post = "https://graph.facebook.com/v13.0/{}/media_publish".format("17841450326370751")
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
    img_dir = "http://34.73.246.95:8000/media/cat_image4.jpg"
    quote = d.get_textdata()
    hashtags = f.fetch()

    caption =  "{}~~~~~~~~~~~~~~~{}".format(quote, hashtags)

    time.sleep(5)
    token = "EAAOaSxfK3vMBAFjLvt5FsriZAoHXJLX4do5eRqJW0mdmzGcmlnFvqD8bffGR7M3Ov7jUTXVFc3YzPrSP4xccr6CdNZBTTrIQfwkpDW7L5zZClYknF8f1kLdN2kwqLUzRS2XMvgXdWx2ZBZAqZCxqm5axXT6iHQLS2aZC0zv0XGTeQZDZD"
    post_url = "https://graph.facebook.com/v13.0/{}/media".format("17841450326370751")
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

        second_post = "https://graph.facebook.com/v13.0/{}/media_publish".format("17841450326370751")
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
    img_dir = "http://34.73.246.95:8000/media/cat_image5.jpg"
    quote = d.get_textdata()
    hashtags = f.fetch()

    caption =  "{}~~~~~~~~~~~~~~~{}".format(quote, hashtags)

    time.sleep(5)
    token = "EAAOaSxfK3vMBAFjLvt5FsriZAoHXJLX4do5eRqJW0mdmzGcmlnFvqD8bffGR7M3Ov7jUTXVFc3YzPrSP4xccr6CdNZBTTrIQfwkpDW7L5zZClYknF8f1kLdN2kwqLUzRS2XMvgXdWx2ZBZAqZCxqm5axXT6iHQLS2aZC0zv0XGTeQZDZD"
    post_url = "https://graph.facebook.com/v13.0/{}/media".format("17841450326370751")
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

        second_post = "https://graph.facebook.com/v13.0/{}/media_publish".format("17841450326370751")
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
    img_dir = "http://34.73.246.95:8000/media/cat_image6.jpg"
    quote = d.get_textdata()
    hashtags = f.fetch()

    caption =  "{}~~~~~~~~~~~~~~~{}".format(quote, hashtags)

    time.sleep(5)
    token = "EAAOaSxfK3vMBAFjLvt5FsriZAoHXJLX4do5eRqJW0mdmzGcmlnFvqD8bffGR7M3Ov7jUTXVFc3YzPrSP4xccr6CdNZBTTrIQfwkpDW7L5zZClYknF8f1kLdN2kwqLUzRS2XMvgXdWx2ZBZAqZCxqm5axXT6iHQLS2aZC0zv0XGTeQZDZD"
    post_url = "https://graph.facebook.com/v13.0/{}/media".format("17841450326370751")
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

        second_post = "https://graph.facebook.com/v13.0/{}/media_publish".format("17841450326370751")
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
    img_dir = "http://34.73.246.95:8000/media/cat_image7.jpg"
    quote = d.get_textdata()
    hashtags = f.fetch()

    caption =  "{}~~~~~~~~~~~~~~~{}".format(quote, hashtags)

    time.sleep(5)
    token = "EAAOaSxfK3vMBAFjLvt5FsriZAoHXJLX4do5eRqJW0mdmzGcmlnFvqD8bffGR7M3Ov7jUTXVFc3YzPrSP4xccr6CdNZBTTrIQfwkpDW7L5zZClYknF8f1kLdN2kwqLUzRS2XMvgXdWx2ZBZAqZCxqm5axXT6iHQLS2aZC0zv0XGTeQZDZD"
    post_url = "https://graph.facebook.com/v13.0/{}/media".format("17841450326370751")
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

        second_post = "https://graph.facebook.com/v13.0/{}/media_publish".format("17841450326370751")
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
    img_dir = "http://34.73.246.95:8000/media/cat_image8.jpg"
    quote = d.get_textdata()
    hashtags = f.fetch()

    caption =  "{}~~~~~~~~~~~~~~~{}".format(quote, hashtags)

    time.sleep(5)
    token = "EAAOaSxfK3vMBAFjLvt5FsriZAoHXJLX4do5eRqJW0mdmzGcmlnFvqD8bffGR7M3Ov7jUTXVFc3YzPrSP4xccr6CdNZBTTrIQfwkpDW7L5zZClYknF8f1kLdN2kwqLUzRS2XMvgXdWx2ZBZAqZCxqm5axXT6iHQLS2aZC0zv0XGTeQZDZD"
    post_url = "https://graph.facebook.com/v13.0/{}/media".format("17841450326370751")
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

        second_post = "https://graph.facebook.com/v13.0/{}/media_publish".format("17841450326370751")
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
    img_dir = "http://34.73.246.95:8000/media/cat_image9.jpg"
    quote = d.get_textdata()
    hashtags = f.fetch()

    caption =  "{}~~~~~~~~~~~~~~~{}".format(quote, hashtags)

    time.sleep(5)
    token = "EAAOaSxfK3vMBAFjLvt5FsriZAoHXJLX4do5eRqJW0mdmzGcmlnFvqD8bffGR7M3Ov7jUTXVFc3YzPrSP4xccr6CdNZBTTrIQfwkpDW7L5zZClYknF8f1kLdN2kwqLUzRS2XMvgXdWx2ZBZAqZCxqm5axXT6iHQLS2aZC0zv0XGTeQZDZD"
    post_url = "https://graph.facebook.com/v13.0/{}/media".format("17841450326370751")
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

        second_post = "https://graph.facebook.com/v13.0/{}/media_publish".format("17841450326370751")
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
    img_dir = "http://34.73.246.95:8000/media/cat_image10.jpg"
    quote = d.get_textdata()
    hashtags = f.fetch()

    caption =  "{}~~~~~~~~~~~~~~~{}".format(quote, hashtags)

    time.sleep(5)
    token = "EAAOaSxfK3vMBAFjLvt5FsriZAoHXJLX4do5eRqJW0mdmzGcmlnFvqD8bffGR7M3Ov7jUTXVFc3YzPrSP4xccr6CdNZBTTrIQfwkpDW7L5zZClYknF8f1kLdN2kwqLUzRS2XMvgXdWx2ZBZAqZCxqm5axXT6iHQLS2aZC0zv0XGTeQZDZD"
    post_url = "https://graph.facebook.com/v13.0/{}/media".format("17841450326370751")
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

        second_post = "https://graph.facebook.com/v13.0/{}/media_publish".format("17841450326370751")
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



def resetMediaPOST(done_with_post):
    if done_with_post is True:
        mediaserver_url = "http://34.73.246.95:8000/media"
        r = requests.delete(mediaserver_url)
        print(r.text)

        print("Waiting 2 minutes until post")

        time.sleep(20)
        folder = "C:\\Users\\fguin\\OneDrive\\Desktop\\instabot\\process\\utils\\content"
        folderdirlist = os.listdir(folder)
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))
        g = ImageGetter()
        g.retrieve_imgs()

        time.sleep(120)

        i = {}

        for i in folderdirlist:
            files = {"file" : open("C:/Users/fguin/OneDrive/Desktop/instabot/process/utils/content/{}".format(i),"rb")}
            l = requests.post(mediaserver_url, files=files)
        print(l.text)
        done_with_post = False
    return done_with_post

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



