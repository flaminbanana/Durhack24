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
url = 'https://www.google.com/search?q=Durham+Attractions&client=firefox-b-d&sca_esv=0d92ac7cb0bb3d0b&sxsrf=ADLYWIKOGEy8xnUBBKHh0RjXANEZ-1FvzQ:1730580577325&udm=15&sa=X&ved=2ahUKEwjW_cOEw76JAxWQSkEAHVbSFSIQxN8JegQIMBAz&biw=1706&bih=807&dpr=1.5'
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
attractions = []
for attraction in soup.find_all('div', class_='ZsAbe EXH1Ce'):
    attractionObj = {}
    name_element = attraction.find('span', class_='Yt787')
    starsRating_element = attraction.find('span', class_='yi40Hd YrbPuc')
    reviewNumber_element = attraction.find('span', class_='RDApEe YrbPuc')
    attractionType0_element = soup.find('div', class_='ZJjBBf cyspcb DH9lqb')
    attractionType_element = attractionType0_element.find('span')

    attractionObj['attractionType'] = attractionType_element.text.strip() if attractionType_element else 'N/A'
    
    attractionObj['name'] = name_element.text.strip() if name_element else 'N/A'
    attractionObj['starsRating'] = starsRating_element.text.strip() if starsRating_element else 'N/A'
    if reviewNumber_element:
        print(f"Original review number text: '{reviewNumber_element.text}'")
        review_number_text = reviewNumber_element.text[1:-1].strip()
        review_number_text = review_number_text.replace(',', '') 
        attractionObj['reviewNumber'] = review_number_text
    else:
        attractionObj['reviewNumber'] = 'N/A'
    
    
    attractions.append(attractionObj)

print(attractions)

filename = 'durhamAttractions.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['name','starsRating','reviewNumber','attractionType'])
    w.writeheader()
    for attraction in attractions:
        w.writerow(attraction)


driver.quit()
