'''
In this program we will be scrapping info from a realestate site and store data like location, area, price in a csv file
Following are the steps performed
1. Get the html for the website to be scraped
2. Get the container of each entry on website
3. Extract fields like title, price etc from the container 
4. Write the fields in a csv file
'''
import requests
from bs4 import BeautifulSoup
from csv import writer

#Url of the page to scrape
url = 'https://www.nobroker.in/property/rent/bangalore/Bellandur?searchParam=W3sibGF0IjoxMi45MzA0Mjc4LCJsb24iOjc3LjY3ODQwNCwicGxhY2VJZCI6IkNoSUpMLWswTG5VVHJqc1JybXFZYjZZMHNzSSIsInBsYWNlTmFtZSI6IkJlbGxhbmR1ciJ9XQ==&radius=2.0&sharedAccomodation=0&city=bangalore&locality=Bellandur'

#################Classes Required to access tags#################
price_id = "minimumRent"
area_class = "font-semibold"
section_class ="bg-white"
title_class = "overflow-hidden"
location_class="mt-0.5p"
################# ################# ################# ############

#Find all sections in the page and look for location and price
page = requests.get(url)

soup = BeautifulSoup(page.content,'html.parser')

#Get all the target tags and store them in a list
lists = soup.select(".bg-white.rounded-4.bg-clip-padding.overflow-hidden")

with open('housing.csv','w',encoding='utf8',newline='') as f:
    thewriter = writer(f)
    header=['Title','Location','Area','Price']
    thewriter.writerow(header)
    for list in lists:
        title = list.find('a', class_=title_class).text
        location = list.find('div', class_=location_class).text
        area_div = list.select(".flex.flex-1.pl-0\.5p")
        area = area_div[0].find('div', class_=area_class).text
        price = list.find(id=price_id).text
        info=[title,location,area,price]
        thewriter.writerow(info)

