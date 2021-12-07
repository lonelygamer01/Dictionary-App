from _typeshed import Self
from tkinter import *
from tkinter.font import BOLD
from tkinter import messagebox as mb
import webbrowser
from googletrans import Translator

translator = Translator()

window = Tk()
window.title("Dictionary.exe")
window.resizable(0,0)
window.geometry("700x550")

textvar = StringVar()

url = "https://www.instagram.com/ez_egy_masik_account/?hl=hu"
def openlink():
        webbrowser.open(url,1)

class Mainsite:
    def __init__(self):
        self.canvas()
        self.title()
        self.Note()
        self.entry()
        self.exit()
        self.submit()
        self.contact()
        self.data_from_entry()
#------------------------------------------------------------------------------------------------------------
    def canvas(self):
        canvas = Canvas(window, bg="steelblue", height=650, width=800)
        canvas.pack()

    def title(self):
        title = Label(window, text="Eng-Hun dictionary", bg="white", fg="red")
        title.config(font=("Comic Sans MS",24, "bold"))
        title.place(relx= 0.26, rely=0.02, height=80, width=330)

    def Note(self):
        question = Label(window, text="NOTE: This app is under development \n please let me know if you have any ideas!\n Make sure you type in the words properly!", bg="white", fg="black")
        question.config(font=("Comic Sans MS",11, "bold"))
        question.place(relx=0.26, rely=0.2, height=130, width=330)

    def entry(self):
        szoveg = Entry(window, textvariable=textvar, justify = CENTER, bd=3, relief="groove")
        szoveg.config(font=('Comic Sans MS', 22))
        szoveg.insert(0, "Enter the word here")
        szoveg.place(relx=0.28, rely=0.5, height=65, width=300)
        entry_text = szoveg.get()
            
    def data_from_entry(self):
             return

        

    def exit(self):
        exit = Button(window, text="Exit", bd=4, command=window.destroy)    
        exit.config(font=("Comic Sans MS",17, "bold"), cursor="hand2")
        exit.place(relx=0.05, rely=0.85, width=100, height=60)


    def submit(self):
        submit = Button(window, text="Translate", bd=4, command=self.translate)
        submit.config(font=("Comic Sans MS",16, "bold"), cursor="hand2")
        submit.place(relx=0.75, rely=0.53,width=120, height=50)


    def translate(self):

        text = translator.translate(entry_text.text)
        
        mb.showwarning(title="Dictionary's message", message=dict.get(text))

    

    def contact(self):
        contact = Button(window, text="Instagram contact", bg="steelblue", bd=0, command=openlink)    
        contact.config(font=("Comic Sans MS",11, "bold"), cursor="hand2")
        contact.place(relx=0.76, rely=0.86,width=150, height=50)

    

        
Mainsite()
window.mainloop()