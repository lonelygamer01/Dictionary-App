from tkinter import *
from tkinter.font import BOLD
from tkinter import messagebox as mb
import webbrowser
from googletrans import Translator
from PIL import ImageTk,Image

window = Tk()
window.title("Dictionary.exe")
window.resizable(0,0)
window.geometry("700x550")

translator = Translator()

textvar = StringVar()

url = "https://www.instagram.com/ez_egy_masik_account/?hl=hu"
def openlink():
        webbrowser.open(url,1)

canvas = Canvas(window, bg="steelblue", height=650, width=800)
canvas.pack()

title = Label(canvas, text="Eng-Hun dictionary", bg="white", fg="red")
title.config(font=("Comic Sans MS",24, "bold"))
title.place(relx= 0.26, rely=0.02, height=80, width=330)

note = Label(canvas, text="NOTE: This app is under development \n please let me know if you have any ideas!\nThere are some bugs in translations\n and it often inaccurate \n(Sorry!)", bg="white", fg="black")
note.config(font=("Comic Sans MS",11, "bold"))
note.place(relx=0.26, rely=0.2, height=130, width=332)

input_text = Entry(canvas, textvariable=textvar, justify = CENTER, bd=3, relief="groove")
input_text.config(font=('Comic Sans MS', 22))
input_text.insert(0, "Enter the word here")
input_text.place(relx=0.28, rely=0.5, height=65, width=300)

exit = Button(canvas, text="Exit", bd=4, command=window.destroy)    
exit.config(font=("Comic Sans MS",17, "bold"), cursor="hand2")
exit.place(relx=0.05, rely=0.85, width=100, height=60)




def translate_hu():
    text = translator.translate(input_text.get(), src="hu", dest="en")
    mb.showinfo(title="Dictionary's message", message=text.text)

def translate_en():
    text = translator.translate(input_text.get(), src="en", dest="hu")
    mb.showinfo(title="Dictionary's message", message=text.text)    

translate_hun = Button(canvas, text="Translate to Eng.", bd=4, command=translate_hu)
translate_hun.config(font=("Comic Sans MS",12, "bold"), cursor="hand2")
translate_hun.place(relx=0.75, rely=0.46,width=160, height=50)

translate_eng = Button(canvas, text="Translate to Hun.", bd=4, command=translate_en)
translate_eng.config(font=("Comic Sans MS",12, "bold"), cursor="hand2")        
translate_eng.place(relx=0.75, rely=0.57,width=160, height=50)

contact = Button(canvas, text="Instagram contact", bg="steelblue", bd=0, command=openlink)    
contact.config(font=("Comic Sans MS",11, "bold"), cursor="hand2")
contact.place(relx=0.76, rely=0.86,width=150, height=50)

image1 = Image.open("C:/Users/User/PycharmProjects/Dictionary App/flag-hungary.jpg")
photo1 = ImageTk.PhotoImage(image1)
hunflag = Label(canvas, image=photo1)    
hunflag.place(width=150, height=150, relx=0.01, rely=0.1)


image2 = Image.open("C:/Users/User/PycharmProjects/Dictionary App/flag-britain.JPEG")
photo2 = ImageTk.PhotoImage(image2)
britflag = Label(canvas, image=photo2)    
britflag.place(width=150, height=150, relx=0.77, rely=0.1)    


window.mainloop()