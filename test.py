from tkinter import *
from tkinter.filedialog import askopenfile

List_types = [ ( "Fichier csv" , ".csv" ) , ( "Fichier json" , ".json" ) , ( "Fichier yaml" , ".yaml" ) , ( "Fichier xml" , ".xml" ) ]

#Create functions
def getFile():
    print("Hello world !")
    file_path = askopenfile(mode='r', filetypes=List_types)
    print(file_path)

    if file_path is not None:
        filename =  str(file_path.name).split('/')[-1]
        print(filename)
        window.destroy
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
btn = Button(frame_text, text="Choisir un fichier", font=("Montserrat", 20), bg="#F05", fg="#fff", 
                height=2, width=20 , bd=2 , activeforeground="#000000", activebackground="#F2F5C8", command=getFile);

btn.pack(pady=40)

#Ajouter le frame
frame_text.pack(expand=YES)


#Affichage
window.mainloop()