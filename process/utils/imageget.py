from email.mime import image
import shutil
from urllib import response
import shutil
import requests
from PIL import Image as img
import os
from pathlib import Path


class ImageGetter():
    def __init__(self):
        self.directory = Path(__file__).resolve().parent
        self.storage = os.path.join(self.directory, 'content') 
    def get_catimg(self):

        n = sum(1 for d in os.listdir(self.storage) if os.path.isfile(os.path.join(self.storage, d)))


        file_name = 'cat_image{}.jpg'.format(n+1) 

        response = requests.get('https://thecatapi.com/api/images/get?format=src&type=gif?api_key=4b44be7a-6781-4962-8bfd-dd7141edd60f', stream=True)
        print(response.text)

        if response.status_code == 200:
            with open(file_name,'wb') as i:
                i.write(response.content)
            print("Done with: ",file_name)
        else:
            print('cant do it')

        shutil.move(file_name, self.storage)
    def retrieve_imgs(self):
        while True:
            ImageGetter.get_catimg(self)
            if len(os.listdir(self.storage)) >= 10:
                break

        

bot = ImageGetter()
bot.retrieve_imgs()












