import json
import yaml
import datetime

print(str(datetime.datetime.now().time()).split('.')[1])

filename = "datas/exemple.json"

with open(filename) as fjson:
    file = json.load(fjson);
    print(file);

    with open(str(datetime.datetime.now().time()).split('.')[1]+'convert.yaml', 'w') as yml:
        yaml.safe_dump(file, yml, allow_unicode=True)
