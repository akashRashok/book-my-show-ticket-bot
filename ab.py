from selenium import webdriver
import time
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

path=r'C:\Program Files (x86)\chromedriver.exe'
driver=webdriver.Chrome(path)
url1='https://in.bookmyshow.com/buytickets/black-panther-wakanda-forever-3d4dx-kochi/movie-koch-ET00342960-MT'
#url2=20221111
#url=url1+str(url2)
driver.get(url1)
cond=0
keyboard=Controller()
baseUrl='https://api.telegram.org/bot5539547339:AAFlL7mzX6WtyXZZApyJaIx4orSY4Mylk7E/sendMessage?chat_id=-842786410&text=Booking Open'


while cond==0:
    ulClass=driver.find_element("id","venuelist")
    venues= ulClass.find_elements_by_tag_name("li")
    for venue in venues:
        venue1="PVR: Lulu, Kochi"
        venue2="PVR: Oberon Mall, Kochi"
        if (venue1 in venue.text) or (venue2 in venue.text):
            cond=1
            requests.get(baseUrl)
            print("boook now")
            break
    if cond==1:
        break
    time.sleep(5)
    driver.get(url1)
driver.quit()


