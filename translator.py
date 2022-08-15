from googletrans import Translator
from gtts import gTTS
from tkinter import *

window = Tk()
window.geometry('600x280')
window.config(bg="black")
e1=Entry(window,bg="white",fg="black",font=("Arial",25,"bold"))
e1.place(x=20,y=20)

def convert_language():
    a1=e1.get()
    t1=Translator()
    t2=click_option.get()
    
    if t2 == "English":
        convert = "en"
    elif t2 == "Hindi":
        convert = "hi"
    elif t2 == "German":
        convert = "de"
   
    trans_text = t1.translate(a1,dest=convert)
    trans_text = trans_text.text
    ob1 = gTTS(text=trans_text, slow=False, lang=convert)
    label_2.config(text=trans_text)

choices = [
    "English",
    "Hindi",
    "German",
    
]
click_option = StringVar()
click_option.set("Select Language")

list_drop = OptionMenu(window,click_option,*choices)
list_drop.configure(background="green",foreground="White",font=('Arial',15,"bold"))
list_drop.place(x=400,y=20)
label_2=Label(window,text="\t\t\t\t\t\t",bg="white",fg="black")
label_2.place(x=0,y=120)
label_2=Label(window,text="Translated text",bg="red",fg="black",font=('Arial',40,"bold"))
label_2.place(x=180,y=120)
Button_1 = Button(window, text="Translate",bg="red",fg="white",font=('Arial',25,"bold"),command=convert_language)
Button_1.place(x=220,y=200)

window.mainloop()
