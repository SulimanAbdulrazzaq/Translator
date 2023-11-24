import customtkinter
from tkinter import *
from translate import Translator

app = customtkinter.CTk()
app.geometry("800x300")
app.title("Translator")
app.config(bg="#06021a")

font1 = ("Arial",18,"bold")

def translate():
    te.delete(0,END)
    fr = v1.get()
    to = v2.get()
    Translatorr = Translator(from_lang=fr,to_lang=to)
    trans = Translatorr.translate(fe.get())
    te.insert(0,trans)



lang = ["english" ,"german","arabic"]

v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
v4 = StringVar()

fl = customtkinter.CTkLabel(app,font=font1,text="From Language",text_color="#FFFFFF",width=20,bg_color="#06021a")
fl.place(x=20,y=30)

tl = customtkinter.CTkLabel(app,font=font1,text="From Language",text_color="#FFFFFF",width=20,bg_color="#06021a")
tl.place(x=500,y=30)


fc  =customtkinter.CTkComboBox(app,values=lang,variable=v1,font = font1,dropdown_hover_color="#00ff00",fg_color="#FFFFFF",text_color="#ed0707",width=150,height=40,bg_color="#06021a")
fc.place(x=20,y=70)

tc  =customtkinter.CTkComboBox(app,values=lang,variable=v2,font = font1,dropdown_hover_color="#00ff00",fg_color="#FFFFFF",text_color="#136b15",width=150,height=40,bg_color="#06021a")
tc.place(x=490,y=70)

fe = customtkinter.CTkEntry(app,textvariable=v3,font=font1,fg_color="#FFFFFF",border_color="#06021a",text_color="#000000",width=300,height=60,bg_color="#06021a")
fe.place(x=20,y=140)

te = customtkinter.CTkEntry(app,textvariable=v4,font=font1,fg_color="#FFFFFF",border_color="#06021a",text_color="#000000",width=300,height=60,bg_color="#06021a")
te.place(x=490,y=140)


trb = customtkinter.CTkButton(app,text="Translate",command=translate,font=font1,text_color="#FFFFFF",fg_color="#07730a",hover_color="#07730a",bg_color="#06021a")
trb.place(x=330,y=220)









app.mainloop()