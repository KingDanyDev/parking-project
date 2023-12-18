import sys
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from funciones_personas import Funciones
sys.path.append("../Controlador")
sys.path.append("../Modelo")
from conexion import Conexion
from Personas import Persona
from Persona_D import Persona_D
def is_empty(a):
    return len(a) == 0

def guardarpersona():
	a=set(enombre.get())
	if (is_empty(a)==True):
		messagebox.showinfo(message="¿Digite el nombre  porfavor?", title="validar nombre")
		enombre.focus_set()
	else:
		m=messagebox.askquestion(message="¿Desea Guardar el registro?", title="Guardar")
		if m=="yes":
			persona1=Persona(nombre=enombre.get(),telefono=etelefono.get(),email=eemail.get(),estado=eestado.get(),tipo=etipo.get())
			Persona_D.insertar(persona1)
			messagebox.showinfo(message="¿Se guardo correctamente el registro?", title="Guardar persona")
			
		else:
			messagebox.showinfo(message="¿El registro no se guardo?", title="Guardar persona")

ventana= Tk()

#******************************** label*******************************
ventana.config(background="white")
ventana.geometry("500x500")
lnombre=Label(ventana,text="Nombre",font=("Roboto Cn",12))
lnombre.grid(row=0,column=0,pady=5,padx=5,sticky="w")
lnombre.config(background="white")

ltelefono=Label(ventana,text="Telefono",font=("Roboto Cn",12))
ltelefono.grid(row=1,column=0,pady=5,padx=5,sticky="w")
ltelefono.config(background="white")

lemail=Label(ventana,text="Email",font=("Roboto Cn",12))
lemail.grid(row=2,column=0,pady=5,padx=5,sticky="w")
lemail.config(background="white")

lestado=Label(ventana,text="Estado",font=("Roboto Cn",12))
lestado.grid(row=3,column=0,pady=5,padx=5,sticky="w")
lestado.config(background="white")

ltipo=Label(ventana,text="Tipo",font=("Roboto Cn",12))
ltipo.grid(row=4,column=0,pady=5,padx=5,sticky="w")
ltipo.config(background="white")
#********************************Entradas**************************************
enombre=Entry(ventana,font=("Roboto Cn",12),width=17,bd=2)
enombre.grid(row=0,column=1)
eemail=Entry(ventana,font=("Roboto Cn",12),width=17,bd=2)
eemail.grid(row=1,column=1)
etelefono=Entry(ventana,font=("Roboto Cn",12),width=17,bd=2)
etelefono.grid(row=2,column=1)
etipo=ttk.Combobox(ventana,font=("Roboto Cn",12),width=15)
etipo.grid(row=3,column=1)
etipo["value"]=["Activo","Inactivo"]

eestado=ttk.Combobox(ventana,font=("Roboto Cn",12),width=15)
eestado.grid(row=4,column=1)
eestado["value"]=["Propietario","Arrendatario","Visitante"]

#*********************************botones**************************************
bguardar=Button(ventana,text="Guardar",command=guardarpersona)
bguardar.grid(row=5,column=0,pady=10,padx=30)
bmodificar=Button(ventana,text="Modificar")
bmodificar.grid(row=5,column=1,pady=10,padx=30)
beliminar=Button(ventana,text="Eliminar")
beliminar.grid(row=5,column=2,pady=10,padx=30)
bsalir=Button(ventana,text="Salir")
bsalir.grid(row=5,column=3,pady=10,padx=20)

ventana.mainloop()