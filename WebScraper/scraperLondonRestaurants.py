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
url = 'https://www.google.com/search?q=london+restaurants&client=firefox-b-d&sca_esv=bc238d30d88dbf83&biw=1707&bih=799&tbm=lcl&ei=ymkmZ_KuMu63hbIPo-DW-Q0&ved=0ahUKEwjyu4yenr6JAxXuW0EAHSOwNd8Q4dUDCAk&uact=5&oq=london+restaurants&gs_lp=Eg1nd3Mtd2l6LWxvY2FsIhJsb25kb24gcmVzdGF1cmFudHMyChAAGIAEGLEDGA0yBxAAGIAEGA0yBhAAGAcYHjIGEAAYBxgeMgcQABiABBgNMgcQABiABBgNMgcQABiABBgNMgcQABiABBgNMgYQABgHGB4yBxAAGIAEGA1I2QlQAFj1CHACeACQAQCYAX-gAcEFqgEDMy40uAEDyAEA-AEBmAIEoALWAcICCBAAGAUYDRgewgIIEAAYCBgNGB6YAwCSBwMzLjGgB8c1&sclient=gws-wiz-local#rlfi=hd:;si:2798106636650523162,l,ChJsb25kb24gcmVzdGF1cmFudHNI9oWn5oywgIAIWh4QARgAGAEiEmxvbmRvbiByZXN0YXVyYW50cyoCCAOSARptb2Rlcm5fZXVyb3BlYW5fcmVzdGF1cmFudKoBSxABKg8iC3Jlc3RhdXJhbnRzKAAyHhABIhr1afWCuEo2zvoNNeuhaciv4HCOYv-AV1MqOzIWEAIiEmxvbmRvbiByZXN0YXVyYW50cw,y,TuAbSSW1fOQ;mv:[[51.5283514,-0.07209499999999999],[51.5049389,-0.20730649999999998]]'
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
restaurants = [] 

for restaurant in soup.find_all('div', class_='VkpGBb'):
    restaurantObj = {}
    name_element = restaurant.find('span', class_='OSrXXb')
    starsRating_element = restaurant.find('span', class_='yi40Hd YrbPuc')
    reviewNumber_element = restaurant.find('span', class_='RDApEe YrbPuc')
    reviewQuote_element = restaurant.find('span', class_='uDyWh OSrXXb btbrud')
    
    restaurantObj['name'] = name_element.text.strip() if name_element else 'N/A'
    restaurantObj['starsRating'] = starsRating_element.text.strip() if starsRating_element else 'N/A'
    if reviewNumber_element:
        print(f"Original review number text: '{reviewNumber_element.text}'")
        review_number_text = reviewNumber_element.text[1:-1].strip()
        review_number_text = review_number_text.replace(',', '') 
        restaurantObj['reviewNumber'] = review_number_text
    else:
        restaurantObj['reviewNumber'] = 'N/A'
    restaurantObj['reviewQuote'] = reviewQuote_element.text[1:].strip() if reviewQuote_element else 'N/A'
    
    restaurants.append(restaurantObj)

print(restaurants)

filename = 'londonRestaurants.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['name','starsRating','reviewNumber','reviewQuote'])
    w.writeheader()
    for restaurant in restaurants:
        w.writerow(restaurant)


driver.quit()
