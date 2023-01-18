from tkinter import *
from tkinter import ttk
import csv


Dollars = {"Euros": 1.08, "Yen": 0.0078}
Euros = {"Dollars": 0.92, "Yen": 0.0072}
Yen = {"Dollars": 128.74, "Euros": 139.37}


def taux():
    taux = 0.0
    if currency1 == 'Dollars':
            taux = Dollars.get(currency2)
    elif currency1 == 'Euros':
            taux = Euros.get(currency2)
    elif currency1 == 'Yen':
            taux = Yen.get(currency2)
    return(taux)

def calcul():
    global montant
    result = 0
    dataframe = ""
    file = open("historique.txt", 'a')
    montant = amount_field.get()
    if currency1 != currency2:
        result = float(montant) / taux()
        convert.set(result)
        file.write(montant + " " + currency1 + " -> " + currency2 + " = " + str(result) + '\n')
    else:
        print("Conversion impossible entre deux mêmes devises")
 
def action(self):
    global currency1
    global currency2
    currency1 = combo.get()
    currency2 = combo2.get()
    return(currency1,currency2)

fenetre = Tk()
fenetre.geometry("300x300")
fenetre.title("convertisseur de monnaie")
amount = StringVar()
convert = StringVar()
label1 = Label(fenetre, text = "Amount")
label1.pack()
amount_field = Entry(textvariable=amount)
amount_field.pack()
label2 = Label(fenetre, text = "From Currency")
label2.pack()
liste = ["Dollars", "Euros", "Yen"]
combo = ttk.Combobox(fenetre, values = liste)
combo.current(0)
combo.pack()
combo.bind("<<ComboboxSelected>>", action)
label3 = Label(fenetre, text = "To Currency")
label3.pack()
combo2 = ttk.Combobox(fenetre, values = liste)
combo2.current(0)
combo2.pack()
combo2.bind("<<ComboboxSelected>>", action)
button = Button(fenetre, text='Convert', command= calcul, height=3)
button.pack()
convert_field = Entry(textvariable=convert)
convert_field.pack()

fenetre.mainloop()
