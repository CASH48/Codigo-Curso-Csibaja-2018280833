import sys
from tkinter import*

def Registrar():
    mtext = ment.get ()
    mlabel2 = Label (mGui, text = mtext).pack ()
    return


    mGui = Tk ()
    ment = StringVar ()

    mGui.geometry ('500x500+450+150')
    mGui.title ('')

    Letra_txt = PhotoImage (file = "Recursos//Letra.png")

    mlabel = Label (mGui, image = Letra_txt). pack ()

    mEntry = Entry (width = 50, justify = CENTER).pack()

    Button (mGui, text = 'Ok', command = Registrar,fg = 'black', bg = 'grey' ).pack ()
