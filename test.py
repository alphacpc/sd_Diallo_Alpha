import xml.etree.ElementTree as et;


with open("datas/dioum.xml") as fxml:
    file = et.parse(fxml);
    root = file.getroot();
    
    
    element = {root.tag: root.attrib if root.attrib else root.text}
    
    hello = root.attrib.keys();
    
    for key in hello:
        print("@"+key, root.attrib[key])

    print(element)

    for child in root:

        # print(child.tag)
        
        if len(child)>0:

            for item in child:
                
                # print(item.tag, child.text)
                pass