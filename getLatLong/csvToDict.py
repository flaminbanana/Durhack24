import csv

def csvToDict(filename):
    with open(filename,'r') as file:
        csvFile = csv.DictReader(file)
        data = [row for row in csvFile]
    return data