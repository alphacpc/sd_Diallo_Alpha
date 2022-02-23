import json;
import yaml;
import xml.etree.ElementTree as et;
import csv;


print('\n\n')
print('******************JSON********************')
print('\n\n')

with open("datas/dioum.json") as fjson:
    file = json.load(fjson);
    print(file);

print('\n\n')
print('******************YAML********************')
print('\n\n')

with open("datas/dioum.yaml") as fyaml:
    file = yaml.safe_load(fyaml);
    print(file);


print('\n\n')
print('****************XML****************')
print('\n\n')

with open("datas/dioum.xml") as fxml:
    file = et.parse(fxml);
    root = file.getroot()
    for child in root:
        print(child.tag, child.text)
        


print('\n\n')
print('****************CSV****************')
print('\n\n')

with open("datas/data.csv") as fcsv:
    reader = csv.DictReader(fcsv);
    for row in reader:
        print(row,'\n')
