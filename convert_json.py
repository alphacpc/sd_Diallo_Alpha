import json
import yaml
import csv
import xml
import datetime

print(str(datetime.datetime.now().time()).split('.')[1])

filename = "datas/exemple.json"

def jsonToyaml():
    with open(filename) as fjson:
        file = json.load(fjson);

    with open(str(datetime.datetime.now().time()).split('.')[1]+'convert.yaml', 'w') as yml:
        yaml.safe_dump(file, yml, allow_unicode=True)



def jsonToxml():
    with open(filename) as fjson:
        file = json.load(fjson);

    with open(str(datetime.datetime.now().time()).split('.')[1]+'convert.yaml', 'w') as yml:
        yaml.safe_dump(file, yml, allow_unicode=True)