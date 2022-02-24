import json
import yaml
import csv
import xml
import datetime

print(str(datetime.datetime.now().time()).split('.')[1])

filename = "datas/dioum.json"

def jsonToyaml(filename):
    with open(filename) as fjson:
        file = json.load(fjson);

    with open(str(datetime.datetime.now().time()).split('.')[1]+'convert.yaml', 'w') as yml:
        yaml.safe_dump(file, yml, allow_unicode=True)



def jsonTocsv(filename):
    with open(filename) as fjson:
        file = json.load(fjson);
        fieldnames = file.keys();

    with open(str(datetime.datetime.now().time()).split('.')[1]+'convert.csv', 'w') as file_csv:
        file_csv = csv.DictWriter(file_csv, fieldnames=fieldnames)
        file_csv.writeheader()
        file_csv.writerow(file)



jsonTocsv(filename)