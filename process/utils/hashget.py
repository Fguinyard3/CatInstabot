from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


#HashFetcher utilized selenium to collect the best hashtags for my post.

class HashFetcher():
    def __init__(self):
        #Having options in optional but is recommended if you dont want to display the window or if running on OS with no GUI
        #--headless argument will allow chromedriver to operate without opening a window (really helps on low RAM instances 
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        #ChromeDriverManager().install() installs chromedriver into the parent directory given its not there
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=self.chrome_options)
        
    
    def fetch(self):
        self.driver.get('http://best-hashtags.com/hashtag/cats/')
        hashtext = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div[2]/div[1]/div/div/div[1]/div[1]/p1').text
        self.driver.close()
        return hashtext







