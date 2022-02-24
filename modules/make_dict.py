import json;
import yaml;
import xml.etree.ElementTree as et;
import csv;
import xmltodict;


######### JSON TO DICT #############
def json_to_dict(filename):
    with open(filename) as fjson:
        file = json.load(fjson);
        print(file)
        return file;


######### YAML TO DICT #############
def yaml_to_dict(filename): 
    with open(filename) as fyaml:
        file = yaml.safe_load(fyaml);
        print(file)
        return file;


######### CSV TO DICT #############
def csv_to_dict(filename): 

    my_dic = dict();

    with open(filename) as fcsv:
        reader = csv.DictReader(fcsv);
        i = 1;

        for row in reader:
            my_dic["elment"+str(i)] = row;
            i += 1
        
        return my_dic


######### XML TO DICT #############
def xml_to_dict(filename):  

    with open(filename) as fxml:
        dic = xmltodict.parse(fxml.read())
        dic = json.loads(json.dumps(dic))
        print(dic)
        return dic;