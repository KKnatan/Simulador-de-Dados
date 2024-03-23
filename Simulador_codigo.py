#Dados

from tkinter import *
from time import sleep
import random

#tela
Tela= Tk()
Tela.title("Dados")
Tela.geometry("400x300")
Tela.configure(bg='#c5cdd4')
Tela.maxsize(400,300)
Tela.minsize(400,300)
#Codigo

pato=StringVar()

def d4():
    numero=random.randint(1,4)
    pato.set(str(numero))
def d6():
    numero=random.randint(1,6)
    pato.set(str(numero))
def d8():
    numero=random.randint(1,8)
    pato.set(str(numero))

def d10():
    numero=random.randint(1,10)
    pato.set(str(numero))
def d12():
    numero=random.randint(1,12)
    pato.set(str(numero))

def d20():
    numero=random.randint(1,20)
    pato.set(str(numero))

def d100():
    numero=random.randint(1,100)
    pato.set(str(numero))

#Layout

texo1=Label(Tela,text='Jogue um',font=("Comfortaa", 35,"bold"),bg='#c5cdd4')
texo1.grid(column=2,row=2,sticky=N,padx=(85,0))

#Botoes
D4= Button(Tela,text='D4',relief=SOLID,width=5,command=d4)
D4.grid(column=2,row=3)

D6= Button(Tela,text='D6',relief=SOLID,width=5,command=d6)
D6.grid(column=2,row=3,padx=(100,0))

D8= Button(Tela,text='D8',relief=SOLID,width=5,command=d8)
D8.grid(column=2,row=3,padx=(205,0))

D10= Button(Tela,text='D10',relief=SOLID,width=5,command=d10)
D10.grid(column=2,row=4,pady=(5,0))

D12= Button(Tela,text='D12',relief=SOLID,width=5,command=d12)
D12.grid(column=2,row=4,pady=(5,0),padx=(100,0))

D20= Button(Tela,text='D20',relief=SOLID,width=5,command=d20)
D20.grid(column=2,row=4,pady=(5,0),padx=(205,0))

D100= Button(Tela,text='D100',relief=SOLID,width=5,command=d100)
D100.grid(column=2,row=5,padx=(100,0),pady=(5,0))


entre= Entry(Tela,textvariable=pato,state="disabled",font=("Arial",15,'bold'),justify=CENTER)
entre.grid(column=2,row=6,padx=(90,0),pady=(10,0))

Tela.mainloop()
