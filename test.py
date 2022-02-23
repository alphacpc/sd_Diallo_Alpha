from tkinter import *
from tkinter.filedialog import askopenfile;
import csv;

import make_dict;

List_types = [ ( "Fichier csv" , ".csv" ) , ( "Fichier json" , ".json" ) , ( "Fichier yaml" , ".yaml" ) , ( "Fichier xml" , ".xml" ) ]

#Create functions
def getFile():

    file_path = askopenfile(mode='r', filetypes=List_types)

    if file_path is not None:
        filename =  str(file_path.name).split('/')[-1]
        print(filename)

        file_entry.delete(0,END);
        file_entry.insert(0,filename);
        
        if "csv" in filename:
            make_dict.csv_to_dict(file_path.name)

        elif "json" in filename:
            make_dict.json_to_dict(file_path.name)
            
        elif "yaml" in filename:
            make_dict.yaml_to_dict(file_path.name)

        elif "xml" in filename:
            make_dict.xml_to_dict(file_path.name)

        else:
            pass


#Creation de fenetre
window = Tk()

#Customize
window.title("Programme de conversion")
window.minsize(980,680)
window.maxsize(1080,720)
window.config(background="#219F94")

#Creation de frames
frame_text = Frame(window, bg="#219F94")
frame_input = Frame(window, bg="#219F94")

#Ajouter du texte
label_title = Label(frame_text, text="CONVERSION", font=("Montserrat",45), fg="#fff", bg="#219F94");
label_title.pack()

label_title = Label(frame_text, text="CSV | JSON | YAML | XML", font=("Montserrat",35), fg="#fff", bg="#219F94");
label_title.pack(pady=10, fill=X)


#Ajouter un bouton
btn = Button(frame_text, text="Choisir un fichier", font=("Montserrat", 20), bg="#F05", fg="#fff", bd=1 , activeforeground="#000000", activebackground="#F2F5C8", command=getFile);
btn.pack(pady=40)

btn_csv = Button(frame_input, text="convertir en csv", font=("Montserrat", 20), bg="#F05", fg="#fff", bd=1 , activeforeground="#000000", activebackground="#F2F5C8");
btn_csv.pack(pady=4)

btn_xml = Button(frame_input, text="convertir en xml", font=("Montserrat", 20), bg="#F05", fg="#fff", bd=1 , activeforeground="#000000", activebackground="#F2F5C8");
btn_xml.pack(pady=4)

btn_json = Button(frame_input, text="convertir en json", font=("Montserrat", 20), bg="#F05", fg="#fff", bd=1 , activeforeground="#000000", activebackground="#F2F5C8");
btn_json.pack(pady=4)

btn_yaml = Button(frame_input, text="convertir en yaml", font=("Montserrat", 20), bg="#F05", fg="#fff", bd=1 , activeforeground="#000000", activebackground="#F2F5C8");
btn_yaml.pack(pady=4)


file_entry = Entry(frame_text, font=("Montserrat",25), fg="#219F94", bg="#FFFFFF" )
file_entry.pack()


#Ajouter le frame
frame_text.pack(expand=YES)
frame_input.pack(expand=YES)


#Affichage
window.mainloop()