import csv
import numpy as np


def getDataSource(data_path):
    marks_In_percentage = []
    Days_Present = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
           marks_In_percentage .append(float(row["marks In percentage"]))
           Days_Present .append(float(row["\tDays Present"]))

    return {"x" : marks_In_percentage, "y": Days_Present}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between marks in percentage and days present :-  \n--->",correlation[0,1])

def setup():
    data_path  = "data.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()
