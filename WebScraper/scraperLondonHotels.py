from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv
import time
import random


option = webdriver.ChromeOptions()
option.add_argument("--incognito")

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
option.add_argument(f"user-agent={user_agent}")

driver = webdriver.Chrome(options=option)  
url = 'https://www.google.com/travel/search?q=london%20hotels&g2lb=4814050%2C4874190%2C4893075%2C4965990%2C4969803%2C72277293%2C72302247%2C72317059%2C72406588%2C72414906%2C72421566%2C72471280%2C72472051%2C72473841%2C72481459%2C72485658%2C72499705%2C72602734%2C72614662%2C72616120%2C72619927%2C72628720%2C72647020%2C72648289%2C72658035%2C72671093%2C72686036%2C72729615%2C72749231%2C72758705%2C72790357%2C72800276&hl=en-GB&gl=uk&cs=1&ssta=1&ts=CAESCgoCCAMKAggDEAAqBwoFOgNHQlA&qs=CAAgACgA&ap=KigKEgnl26ydJ65JQBEgK9p3QKDYvxISCaPxIMnwxElAEYBTlyD-M7U_MABoAQ&ictx=111&ved=0CAAQ5JsGahgKEwj4qaT6lb6JAxUAAAAAHQAAAAAQiAE'
driver.get(url)

# simulate user behaviour by waitinelg randomly
time.sleep(random.uniform(2, 4)) 


# randomly scroll to simulate human behaviour
for i in range(5):
    driver.execute_script("window.scrollBy(0, 300);")
    time.sleep(random.uniform(1, 3)) 

sitehtml = driver.page_source
soup = BeautifulSoup(sitehtml, 'html.parser')

# Store data in a dictionary for easier conversion to a CSV file
hotels = []
for hotel in soup.find_all('div', class_='uaTTDe BcKagd bLc2Te Xr6b1e'):
    hotelObj = {}
    name_element = hotel.find('h2', class_='BgYkof ogfYpf ykx2he')
    starsRating_element = hotel.find('span', class_='KFi5wf lA0BZ')
    reviewNumber_element = hotel.find('span', class_='jdzyld XLC8M')
    price_element = hotel.find('span', class_='qQOQpe prxS3d')
    
    hotelObj['name'] = name_element.text.strip() if name_element else 'N/A'
    hotelObj['starsRating'] = starsRating_element.text.strip() if starsRating_element else 'N/A'
    if reviewNumber_element:
        print(f"Original review number text: '{reviewNumber_element.text}'")
        review_number_text = reviewNumber_element.text[2:-1].strip()
        review_number_text = review_number_text.replace(',', '') 
        hotelObj['reviewNumber'] = review_number_text
    else:
        hotelObj['reviewNumber'] = 'N/A'
    hotelObj['price'] = price_element.text[1:].strip() if price_element else 'N/A'
    
    hotels.append(hotelObj)

print(hotels)

filename = 'londonHotels.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['name','starsRating','reviewNumber','price'])
    w.writeheader()
    for hotel in hotels:
        w.writerow(hotel)


driver.quit()
