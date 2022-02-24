import xmltodict;
import json;

f = open("datas/dioum.xml", "r");
dic = xmltodict.parse(f.read())
dic = json.loads(json.dumps(dic))
print(dic)