import csv

myPath = "/home/alpha/Projects/convertisseur/datas/data.csv"
result = myPath.split("/")
print(myPath)
print(result)


with open(myPath) as fcsv:
    reader = csv.DictReader(fcsv);
    for row in reader:
        print(row,'\n');
