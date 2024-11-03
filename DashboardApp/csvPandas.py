import pandas as pd
import numpy as np

def requestData(location, category):
    # returns dataframe object of csv file corresponding to request
    catname = category.capitalize()
    filename = location + catname + ".csv"
    df = pd.read_csv("scrapedData/" + filename)
    return df

#def sortData(criteria):

