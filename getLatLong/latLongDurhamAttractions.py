import csvToDict
import requests
import urllib.parse
import csv

Dict = csvToDict.csvToDict('scrapedData/durhamAttractions.csv')
Name = [item['name'] for item in Dict]
Name = [item + ' Durham UK' for item in Name]

coordinates = []

for i in range(len(Name)):
    address = Name[i]
    url = 'https://nominatim.openstreetmap.org/search?q=' + urllib.parse.quote(address) +'&format=json'

    response = requests.get(url)
    data = response.json()
    if data:
        coordinate = data[0]["lat"]+','+data[0]["lon"]
        coordinates.append(coordinate)
    else:
        coordinates.append('N/A')

for i in range(len(Dict)):
    Dict[i]['coordinates'] = coordinates[i]

with open('scrapedData/durhamAttractions.csv', 'w', newline='') as file:
    fieldnames = Dict[0].keys()
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(Dict)

print("CSV file updated successfully.")
