import json
import yaml
import csv
import xml
import datetime



def convert_to_yaml(my_dict):

    with open(str(datetime.datetime.now().time()).split('.')[1]+'convert.yaml', 'w') as yml:
        yaml.safe_dump(my_dict, yml, allow_unicode=True) 






def convert_to_csv(my_dict):

    fieldnames = my_dict.keys()

    with open(str(datetime.datetime.now().time()).split('.')[1]+'convert.csv', 'w') as file_csv:
        file_csv = csv.DictWriter(file_csv, fieldnames=fieldnames)
        file_csv.writeheader()
        file_csv.writerow(my_dict)





def convert_to_json(my_dict):

    with open(str(datetime.datetime.now().time()).split('.')[1]+'convert.json', 'w') as jsn:
        json.dumps(my_dict, jsn)
