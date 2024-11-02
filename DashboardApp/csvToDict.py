import csv

def csvToDict(filename):
    with open(filename,'r') as file:
        csvFile = csv.DictReader(file)
        data = [row for row in csvFile]
    return data

#To use: do acording to example : durhamAttractions = csvToDict('scrapedData/durhamAttractions.csv')
#Output will be a dictionary with the data from the csv file, visualise data accordingly.