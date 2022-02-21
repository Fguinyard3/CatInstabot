import shutil
from urllib import response
import shutil
import requests
import os
from pathlib import Path


class ImageGetter():
    def __init__(self):
        #Tells each instance what to set the recieving folder to
        self.directory = Path(__file__).resolve().parent
        self.storage = os.path.join(self.directory, 'content') 
    def get_catimg(self):
        #Here, n will be determine based on the the amount of files in the directory.
        #This helps the function create duplicate named images just by formatting the end of the file name 
        n = sum(1 for d in os.listdir(self.storage) if os.path.isfile(os.path.join(self.storage, d)))


        file_name = 'cat_image{}.jpg'.format(n+1) 
        #Get image from thecatapi's API
        response = requests.get('https://thecatapi.com/api/images/get?format=src&type=gif?api_key=<YOUR API KEY FOR thecatapi >', stream=True)
        print(response.text)
        #Write file and moves it to content folder
        if response.status_code == 200:
            with open(file_name,'wb') as i:
                i.write(response.content)
            print("Done with: ",file_name)
        else:
            print('cant do it')

        shutil.move(file_name, self.storage)
    def retrieve_imgs(self):
        #Simple loop that calls get_catimg() until the content folder has 10 files. Still has bugs to be worked out.
        while True:
            ImageGetter.get_catimg(self)
            if len(os.listdir(self.storage)) >= 10:
                break

       












