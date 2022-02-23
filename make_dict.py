import json;
import yaml;
import xml.etree.ElementTree as et;
import csv;


def json_to_dict(filename):
    with open(filename) as fjson:
        file = json.load(fjson);
        print(file);




def yaml_to_dict(filename): 
    with open(filename) as fyaml:
        file = yaml.safe_load(fyaml);
        print(file);



def xml_to_dict(filename):
    with open(filename) as fxml:
        file = et.parse(fxml);
        root = file.getroot()
        for child in root:
            print(child.tag, child.text)
            if len(child)>0:
                for item in child:
                    print(item.tag, child.text)




def csv_to_dict(filename):  
    with open(filename) as fcsv:
        reader = csv.DictReader(fcsv);
        for row in reader:
            print(row,'\n')