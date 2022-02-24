from tkinter import *
from tkinter.filedialog import askopenfile

import modules.make_dict as make_dict ;
import modules.transform as transform;

List_types = [ ( "Fichier csv" , ".csv" ) , ( "Fichier json" , ".json" ) , ( "Fichier yaml" , ".yaml" ) , ( "Fichier xml" , ".xml" ) ]

#FUNCTION GET FILE
def getFile():

    global file_path
    global dictname

    file_path = askopenfile(mode='r', filetypes=List_types).name

    if file_path is not None:
        global filename
        filename =  str(file_path).split('/')[-1]

        file_entry.delete(0,END);
        file_entry.insert(0,filename);
        
        if "csv" in filename:
            dictname = make_dict.csv_to_dict(file_path)

        elif "json" in filename:
            dictname = make_dict.json_to_dict(file_path)
            
        elif "yaml" in filename:
            dictname = make_dict.yaml_to_dict(file_path)

        elif "xml" in filename:
            dictname = make_dict.xml_to_dict(file_path)


# CALL CONVERT FUNCTIONS          
def toYaml():
    transform.convert_to_yaml(dictname);

def toCsv():
    transform.convert_to_csv(dictname);

def toXml():
    transform.convert_to_xml(dictname);

def toJson():
    transform.convert_to_json(dictname);


#CREATE WINDOW
window = Tk()

#CUSTOMIZER WINDOW
window.title("Programme de conversion")
window.minsize(980,680)
window.maxsize(1080,720)
window.config(background="#219F94")

#CREATE FRAMES
frame_text = Frame(window, bg="#219F94")
frame_input_first = Frame(window, bg="#219F94")
frame_input_second = Frame(window, bg="#219F94")

#ADD LABEL
label_title = Label(frame_text, text="CONVERSION", font=("Montserrat",45), fg="#fff", bg="#219F94");
label_title.pack()

label_title = Label(frame_text, text="CSV | JSON | YAML | XML", font=("Montserrat",35), fg="#fff", bg="#219F94");
label_title.pack(pady=10, fill=X)


#BUTTON CHOICE FILE AND SHOW ENTRY
btn = Button(frame_text, text="Choisir un fichier", font=("Montserrat", 20), bg="#F05", fg="#fff", bd=1 , activeforeground="#000000", activebackground="#F2F5C8", command=getFile);
btn.pack(pady=40, side=RIGHT)

file_entry = Entry(frame_text, font=("Montserrat",25), fg="#219F94", bg="#FFFFFF" )
file_entry.pack(side=LEFT)

#BUTTONS FOR ALL METHODS CONVERT
btn_csv = Button(frame_input_first, text="convertir en csv", font=("Montserrat", 20), bg="#F05", fg="#fff", bd=1 , activeforeground="#000000", activebackground="#F2F5C8", width=15, command=toCsv);
btn_csv.pack(side=LEFT)

btn_xml = Button(frame_input_first, text="convertir en xml", font=("Montserrat", 20), bg="#F05", fg="#fff", bd=1 , activeforeground="#000000", activebackground="#F2F5C8", width=15, command=toXml);
btn_xml.pack(side=RIGHT)

btn_json = Button(frame_input_second, text="convertir en json", font=("Montserrat", 20), bg="#F05", fg="#fff", bd=1 , activeforeground="#000000", activebackground="#F2F5C8", width=15, command=toJson);
btn_json.pack(side=LEFT)

btn_yaml = Button(frame_input_second, text="convertir en yaml", font=("Montserrat", 20), bg="#F05", fg="#fff", bd=1 , activeforeground="#000000", activebackground="#F2F5C8", width=15, command=toYaml);
btn_yaml.pack(side=RIGHT)

#SHOW FRAMES
frame_text.pack(expand=YES)
frame_input_first.pack(expand=YES)
frame_input_second.pack( expand=YES)

#SHOW WINDOWS
window.mainloop()