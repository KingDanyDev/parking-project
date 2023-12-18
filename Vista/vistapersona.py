from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
"""
from PersonalDao import Persona_D
from Persona import Persona 
from MarcaDao import Marca_D
from Marca import Marca
from Modelo import Modelo
from ModeloDao import Modelo_D
from ColorDao import Color_D
from Color import Color
from Automovil import Automovil
from AutomovilDao import Automovil_D
from conexion import Conexion 
from proyecto import log
from PIL import Image
from PIL import ImageTk
import cv2
import imutils
def is_empty(a):
    return len(a) == 0

#*************************************************************************************
#*                     ELIMINA REGISTROS DE LOS USUARIOS                             *
#*************************************************************************************
def eliminarpersona():
	m=messagebox.askquestion(message="¿Desea Eliminar el registro?", title="Eliminar")
	if m=="yes":
		persona1=Persona(cedula=entrada_cedula.get())
		personas_insertadas=Persona_D.eliminar(persona1)
		limpiarpersona()
		messagebox.showinfo(message="¿Se Elimino el registro?", title="Eliminar persona")
		desactivarlabelyentradaspersona()
		entrada_cedula.focus_set()
	else:
		messagebox.showinfo(message="¿El registro no se Elimino?", title="Eliminar persona")
#****************************************************************************************
#*                     MODIFICA LOS  REGISTROS DE LOS USUARIOS                          *
#****************************************************************************************
def editarpersona():
	m=messagebox.askquestion(message="¿Desea Editar el registro?", title="Guardar")
	if m=="yes":
		persona1=Persona(nombre=entrada_nombre.get(),apellido=entrada_apellido.get(),telefono=entrada_telefono.get(),tipo=entrada_tipo_cb.get(),cedula=entrada_cedula.get())
		personas_insertadas=Persona_D.update(persona1)
		limpiarpersona()
		messagebox.showinfo(message="¿Se Edito correctamente el registro?", title="Editar persona")
		desactivarlabelyentradaspersona()
		entrada_cedula.focus_set()
	else:
		messagebox.showinfo(message="¿El registro no se guardo?", title="Editar persona")
#******************************************************************************************
#                       GUARDA LOS REGISTROS DE LOS USUARIOS                              *
#******************************************************************************************
"""
def guardarpersona():
	a=set(entrada_nombre.get())
	if (is_empty(a)==True):
		messagebox.showinfo(message="¿Digite el nombre  porfavor?", title="validar nombre")
		entrada_nombre.focus_set()
	elif entrada_apellido.get()=="":
		messagebox.showinfo(message="¿Digite el apellido  porfavor?", title="validar apellido")
		entrada_apellido.focus_set()
	else:
		m=messagebox.askquestion(message="¿Desea Guardar el registro?", title="Guardar")
		if m=="yes":
			persona1=Persona(cedula=entrada_cedula.get(),nombre=entrada_nombre.get(),apellido=entrada_apellido.get(),telefono=entrada_telefono.get(),tipo=entrada_tipo_cb.get())
			personas_insertadas=Persona_D.insertar(persona1)
			limpiarpersona()
			messagebox.showinfo(message="¿Se guardo correctamente el registro?", title="Guardar persona")
			desactivarlabelyentradaspersona()
			entrada_cedula.focus_set()
		else:
			messagebox.showinfo(message="¿El registro no se guardo?", title="Guardar persona")
#*********************************************************************************************
#                           ELIMINA LOS REGISTROS DE LOS AUTOS
#*********************************************************************************************
def eliminarautos():
	m=messagebox.askquestion(message="¿Desea Eliminar el registro?", title="Eliminar automovil")
	if m=="yes":
		auto1=Automovil(placa=entrada_placa.get())
		autos_insertados=Automovil_D.eliminar(auto1)
		limpiarautomovil()
		messagebox.showinfo(message="¿Se Elimino el registro?", title="Eliminar automovil")
		#desactivarlabelyentradaspersona()
		entrada_cedula.focus_set()
	else:
		messagebox.showinfo(message="¿El registro no se Elimino?", title="Eliminar automovil")
#************************************************************************************************
#                             MODIFICA LOS REGISTROS DE LOS AUTOS
#***********************************************************************************************
def editarautos():
	m=messagebox.askquestion(message="¿Desea Editar el registro?", title="Editar autos")
	if m=="yes":
		auto1=Automovil(id_marca=entrada_marcados.get(),id_modelo=entrada_modelodos.get(),id_color=entrada_colordos.get(),estado=entrada_estado_auto.get(),placa=entrada_placa.get())
		autos_insertados=Automovil_D.update(auto1)
		limpiarautomovil()
		messagebox.showinfo(message="¿Se Edito correctamente el registro?", title="Editar autos")
		desactivarlabelyentradasdelautomovil()
		entrada_placa.focus_set()
	else:
		messagebox.showinfo(message="¿El registro no se editoo?", title="Editar Automovil")
#*******************************************************************************************
#*                      GUARDA LOS REGISTROS DE LOS AUTOS                                  *
#*******************************************************************************************
def guardarauto():
	a=set(entrada_placa.get())
	if (is_empty(a)==True):
		messagebox.showinfo(message="¿Digite la placa del Automovil?", title="validar placa")
		entrada_marca.focus_set()
	else:
		m=messagebox.askquestion(message="¿Desea Guardar el registro?", title="Guardar Automovil")
		if m=="yes":
			auto1=Automovil(id_persona=entrada_id_p.get(),id_marca=entrada_marcados.get(),id_modelo=entrada_modelodos.get(),id_color=entrada_colordos.get(),placa=entrada_placa.get(),estado=entrada_estado_auto.get())
			autos_insertados=Automovil_D.insertar(auto1)
			limpiarautomovil()
			messagebox.showinfo(message="¿Se guardo correctamente el registro?", title="Guardar Automovil")
			desactivarlabelyentradasdelautomovil()
			entrada_id_p.focus_set()
		else:
			smessagebox.showinfo(message="¿El registro no se guardo?", title="Guardar Automovil")
	#*******************************************************************************************
	#*                                  VALIDA PLACAS                                          *
	#*******************************************************************************************
def validaplacautomovil(event=None):
	a=set(entrada_placa.get())
	vali=entrada_placa.get()
	if (is_empty(a)==True):
		messagebox.showinfo(message="¿Digite la placa porfavor?", title="validar placa")
		entrada_placa.focus_set()
	elif (vali.isalnum()==False):
		messagebox.showinfo(message="¿Digite  tres Letras y tres numeros?", title="validar placa")
		entrada_placa.delete(0,END)
		entrada_placa.focus_set()
	else:
		activarlabelyentradasdelautomovil()
		auto1=Automovil(id_persona=entrada_id_p.get(),placa=entrada_placa.get())
		auto2=Automovil_D.validaplaca(auto1)
		if auto2==[]:
			messagebox.showinfo(message="¿la placa no esta registrada en el sistema?", title="Validar placa")
			entrada_marca.focus_set()
		else:
			messagebox.showinfo(message="¿la placa  esta registrada en el sistema?", title="Validar placa")
			for i in auto2:
				marca1.set(i[0])
				color1.set(i[1])
				modelo1.set(i[2])
				estado1.set(i[3])
				marcarespuesta.set(i[4])
				colorespuesta.set(i[5])
				modelorespuesta.set(i[6])
			boton_guardar_automovil.config(state=DISABLED)
			boton_modificar_automovil.config(state=NORMAL)
			boton_eliminar_automovil.config(state=NORMAL)
			entrada_placa.focus_set()
	#*************************************************************************
	#*                     VALIDA LAS CEDULAS                                *
	#*************************************************************************
def validaridpersona(event=None):
	a=set(entrada_cedula.get())
	vali=entrada_cedula.get()
	if (is_empty(a)==True):
		messagebox.showinfo(message="¿Digite la cedula porfavor?", title="validar campo")
		entrada_cedula.focus_set()
	elif (vali.isdigit()==False):
		messagebox.showinfo(message="¿Digite  numeros porfavor?", title="validar campo")
		entrada_cedula.delete(0,END)
		entrada_cedula.focus_set()
	else:
		activarlabelyentradaspersona()
		persona1=Persona(cedula=entrada_cedula.get())
		persona=Persona_D.validacedula(persona1)
		if persona==[]:
			messagebox.showinfo(message="¿la cedula no esta registrada en el sistema?", title="Validar cedula")
			entrada_nombre.focus_set()
		else:
			for i in persona:
				nombre1.set(i[2])	
				apellido1.set(i[3])
				telefono1.set(i[4])
				usuario1.set(i[5])
			messagebox.showinfo(message="¿la cedula  esta registrada en el sistema?", title="Validar cedula")
			boton_guardar_persona.config(state=DISABLED)
			boton_modificar_persona.config(state=NORMAL)
			boton_eliminar_persona.config(state=NORMAL)
			entrada_nombre.focus_set()
#********************************************************************************************************
#                              GUARDA LAS MARCAS DE LOS AUTOMOVILES                                     *
#********************************************************************************************************
def guardamarca():
	a=set(entrada_marcatres.get())
	if (is_empty(a)==True):
		messagebox.showinfo(message="¿Digite la marca porfavor?", title="valida marca")
		entrada_nombre.focus_set()
	else:
		m=messagebox.askquestion(message="¿Desea Guardar el registro?", title="Guardar marca")
		if m=="yes":
			marca1=Marca(marca=entrada_marcatres.get())
			personas_insertadas=Marca_D.insertar(marca1)
			limpiarmarca()
			messagebox.showinfo(message="¿Se guardo correctamente el registro?", title="Guardar marca")
			desactivarlabelyentradaspersona()
			entrada_marcatres.focus_set()
		else:
			messagebox.showinfo(message="¿El registro no se guardo?", title="Guardar marca")
#********************************************************************************************************
#                              GUARDA LOS COLORES DE LOS AUTOMOVILES                                     *
#********************************************************************************************************
def guardacolor():
	a=set(entrada_colortres.get())
	if (is_empty(a)==True):
		messagebox.showinfo(message="¿Digite el color porfavor?", title="valida color")
		entrada_colortres.focus_set()
	else:
		m=messagebox.askquestion(message="¿Desea Guardar el registro?", title="Guardar color")
		if m=="yes":
			color1=Color(color=entrada_colortres.get())
			personas_insertadas=Color_D.insertar(color1)
			
			messagebox.showinfo(message="¿Se guardo correctamente el registro?", title="Guardar color")
			desactivarlabelyentradaspersona()
			entrada_marcatres.focus_set()
		else:
			messagebox.showinfo(message="¿El registro no se guardo?", title="Guardar color")
#********************************************************************************************************
#                              GUARDA LOS  MODELOS DE LOS AUTOMOVILES                                     *
#********************************************************************************************************
def guardarmodelo():
	a=set(entrada_modelotres.get())
	if (is_empty(a)==True):
		messagebox.showinfo(message="¿Digite el color porfavor?", title="valida modelo")
		entrada_modelotres.focus_set()
	else:
		m=messagebox.askquestion(message="¿Desea Guardar el registro?", title="Guardar modelo")
		if m=="yes":
			modelo1=Modelo(modelo=entrada_modelotres.get())
			personas_insertadas=Modelo_D.insertar(modelo1)
			
			messagebox.showinfo(message="¿Se guardo correctamente el registro?", title="Guardar modelo")
			desactivarlabelyentradaspersona()
			entrada_modelotres.focus_set()
		else:
			messagebox.showinfo(message="¿El registro no se guardo?", title="Guardar modelo")

def ejecutanombre(event=None):
	persona1=Persona(id_persona=entrada_id_p.get())
	persona=Persona_D.consultanomape(persona1)
	for i in persona:
		texto.set(i[0]+" "+i[1])
	entrada_placa.focus_set()

def ejecutamarca(event=None):
	marca1=Marca(marca=entrada_marca.get())
	marcass=Marca_D.consultamarca(marca1)
	for i in marcass:
		marcarespuesta.set(i[0])
def ejecutamodelo(event=None):
	modelo1=Modelo(modelo=entrada_modelo.get())
	modeloss=Modelo_D.consultamodelo(modelo1)
	for i in modeloss:
		modelorespuesta.set(i[0])
def ejecutacolor(event=None):
	color1=Color(color=entrada_color.get())
	coloress=Color_D.consultacolor(color1)
	for i in coloress:
		colorespuesta.set(i[0])


	#limpia las entradas de la ventana Persona
def limpiarpersona():
	entrada_cedula.delete(0,END)
	entrada_nombre.delete(0,END)
	entrada_apellido.delete(0,END)
	entrada_telefono.delete(0,END)
	entrada_tipo_cb.delete(0,END)
	entrada_cedula.focus_set()
	#limpia las entradas de la ventana  Automovil
def limpiarautomovil():
	entrada_nombress.delete(0,END)
	entrada_placa.delete(0,END)
	entrada_marca.delete(0,END)
	entrada_modelo.delete(0,END)
	entrada_color.delete(0,END)
	entrada_estado_auto.delete(0,END)
	entrada_id_p.focus_set()
	#ACTIVA LOS LABEL, LAS ENTRADAS Y LOS BOTONES DE LA VENTANA PERSONA
def activarlabelyentradaspersona():	
	entrada_nombre.config(state=NORMAL)
	entrada_apellido.config(state=NORMAL)
	entrada_telefono.config(state=NORMAL)
	entrada_tipo_cb.config(state=NORMAL)
	boton_guardar_persona.config(state=NORMAL)
	
#DESACTIVA LOS LABEL, LAS ENTRADAS Y LOS BOTONES DE LA VENTANA PERSONA
def desactivarlabelyentradaspersona():	
	entrada_nombre.config(state=DISABLED)
	entrada_apellido.config(state=DISABLED)
	entrada_telefono.config(state=DISABLED)
	entrada_tipo_cb.config(state=DISABLED)
	boton_guardar_persona.config(state=DISABLED)
	boton_modificar_persona.config(state=DISABLED)
	boton_eliminar_persona.config(state=DISABLED)
	#ACTIVA LOS LABEL, LAS ENTRADAS Y LOS BOTONES DE LA VENTANA AUTOMOVIL
def activarlabelyentradasdelautomovil():
	entrada_marca.config(state=NORMAL)
	entrada_modelo.config(state=NORMAL)
	entrada_color.config(state=NORMAL)
	entrada_estado_auto.config(state=NORMAL)
	boton_guardar_automovil.config(state=NORMAL)
	
	#DESACTIVA LOS LABEL, LAS ENTRADAS Y LOS BOTONES DE LA VENTANA AUTOMOVIL
def desactivarlabelyentradasdelautomovil():
	entrada_marca.config(state=DISABLED)
	entrada_modelo.config(state=DISABLED)
	entrada_color.config(state=DISABLED)
	entrada_estado_auto.config(state=DISABLED)
	boton_guardar_automovil.config(state=DISABLED)
	boton_modificar_automovil.config(state=DISABLED)
	boton_eliminar_automovil.config(state=DISABLED)
	#abre la ventana persona
def abrirventanapersonas():
	ventana_padre.withdraw()
	ventana_persona.deiconify()
	entrada_cedula.focus_set()
	#cierra la ventana persona
def cerrarventanapersonas():
	ventana_persona.withdraw()
	ventana_padre.deiconify()
	#abre la ventana autos
def abrirventanautos():
	ventana_padre.withdraw()
	entrada_nombress.config(state=DISABLED)
	entrada_id_p.focus_set()
	ventana_autos.deiconify()
	#cerrar la ventana autos
def cerrarventanautos():
	ventana_autos.withdraw()
	ventana_padre.deiconify()
	#abre la ventana parqueadero
def abrirventanahistorial():
	ventana_padre.withdraw()
	ventana_historial.deiconify()
	
def cerrarventanahistorial():
	ventana_historial.withdraw()
	ventana_padre.deiconify()

def abrirventanamarca():
	ventana_padre.withdraw()
	ventana_marca.deiconify()
	
def cerrarventanamarca():
	ventana_marca.withdraw()
	ventana_padre.deiconify()

def abrirventanacolor():
	ventana_padre.withdraw()
	ventana_color.deiconify()
	
def cerrarventanacolor():
	ventana_color.withdraw()
	ventana_padre.deiconify()

def abrirventanamodelo():
	ventana_padre.withdraw()
	ventana_modelo.deiconify()
	
def cerrarventanamodelo():
	ventana_modelo.withdraw()
	ventana_padre.deiconify()


#***********************VENTANA PADRE E HIJAS**********************
ventana_padre=Tk()
ventana_padre.resizable(width=False,height=False)
ventana_padre.geometry("1100x500")

texto=StringVar()
nombre1=StringVar()
apellido1=StringVar()
telefono1=IntVar()
usuario1=StringVar()

marca1=StringVar()
marcarespuesta=IntVar()
modelo1=StringVar()
modelorespuesta=IntVar()
color1=StringVar()
colorespuesta=IntVar()
estado1=StringVar()

ventana_padre.iconbitmap("imagenes/logo.ico")
ventana_padre.title("Menu Principal")

ventana_persona=Toplevel(ventana_padre)
ventana_persona.withdraw()
ventana_persona.iconbitmap("imagenes/logo.ico")
ventana_autos=Toplevel(ventana_padre)
ventana_autos.withdraw()
ventana_autos.iconbitmap("imagenes/logo.ico")

ventana_historial=Toplevel(ventana_padre)
ventana_historial.withdraw()
ventana_historial.iconbitmap("imagenes/logo.ico")

ventana_marca=Toplevel(ventana_padre)
ventana_marca.withdraw()
ventana_marca.iconbitmap("imagenes/logo.ico")

ventana_color=Toplevel(ventana_padre)
ventana_color.withdraw()
ventana_color.iconbitmap("imagenes/logo.ico")

ventana_modelo=Toplevel(ventana_padre)
ventana_modelo.withdraw()
ventana_modelo.iconbitmap("imagenes/logo.ico")

#**********************MENU PRINCIPAL******************************
barra=Menu()
usuario=Menu(barra,tearoff=0)
usuario.add_command(label="Nuevo Usurio",command=abrirventanapersonas)
usuario.add_separator()
usuario.add_command(label="Salir",command=ventana_padre.quit)
auto=Menu(barra,tearoff=0)
auto.add_command(label="Nuevo Automovil ",command=abrirventanautos)
auto.add_command(label="Marca ",command=abrirventanamarca)
auto.add_command(label="Modelo ",command=abrirventanamodelo)
auto.add_command(label="Color ",command=abrirventanacolor)
historia=Menu(barra,tearoff=0)
historia.add_command(label="Registro Historico ",command=abrirventanahistorial)
barra.add_cascade(label="Usuarios", menu=usuario)
barra.add_cascade(label="Automoviles",menu=auto)
barra.add_cascade(label="Historial",menu=historia)
#
img=cv2.imread('imagenes/cabecera.png')
img=imutils.resize(img,width=1100)
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img=Image.fromarray(img)
image=ImageTk.PhotoImage(image=img)
fondo=Label(ventana_padre,image=image).place(x=0,y=0)
ventana_padre.config(menu=barra)
#*********************ETIQUETAS DE LA VENTANA DATOS PERSONALES****************************
ventana_persona.title("Registro de Usuarios")
ventana_persona.geometry("500x350")
ventana_persona.config(background="white")
imgcabecera=Image.open("imagenes/cabecera.png")
imgcabecera = imgcabecera.resize((480,100), Image.Resampling.LANCZOS)
imgcabecera=ImageTk.PhotoImage(imgcabecera)
cabeza = Label(ventana_persona,image=imgcabecera)
cabeza.config(background="white")
cabeza.pack()
lblFrame_persona = LabelFrame(ventana_persona)
lblFrame_persona.place(x= 10, y=110, width= 480)
lblFrame_persona.config(background="white")
lblFrame_persona_botones = LabelFrame(ventana_persona)
lblFrame_persona_botones.place(x= 10, y= 250,width= 480)
lblFrame_persona_botones.config(background="white")

label_cedula=Label(lblFrame_persona,text="Cedula",  font=("Roboto Cn",12))
label_cedula.grid(row=0,column=0,pady=10,padx=5,sticky="w")
label_cedula.cget('relief')
label_cedula.config(background="white")
label_nombre=Label(lblFrame_persona,text="Nombre",font=("Roboto Cn",12))
label_nombre.grid(row=1,column=0,pady=5,padx=5,sticky="w")
label_nombre.config(background="white")
label_apellido=Label(lblFrame_persona,text="Apellido",font=("Roboto Cn",12))
label_apellido.grid(row=1,column=2,pady=5,padx=5)
label_apellido.config(background="white")
label_telefono=Label(lblFrame_persona,text="Telefono",font=("Roboto Cn",12))
label_telefono.grid(row=2,column=0,pady=10,padx=5)
label_telefono.config(background="white")
label_tipo_usuario=Label(lblFrame_persona,text="Usuario",font=("Roboto Cn",12))
label_tipo_usuario.grid(row=2,column=2,pady=5,padx=5)
label_tipo_usuario.config(background="white")
#*********************ENTRADAS DE LA VENTANA DATOS PERSONALES********************************
entrada_cedula=Entry(lblFrame_persona,font=("Roboto Cn",12),width=17,bd=2)
entrada_cedula.grid(row=0,column=1)
entrada_nombre=Entry(lblFrame_persona,textvariable=nombre1,font=("Roboto Cn",12),width=17,bd=2)
entrada_nombre.grid(row=1,column=1)
entrada_apellido=Entry(lblFrame_persona,textvariable=apellido1,font=("Roboto Cn",12),width=17,bd=2)
entrada_apellido.grid(row=1,column=3)
entrada_telefono=Entry(lblFrame_persona,textvariable=telefono1,font=("Roboto Cn",12),width=17,bd=2)
entrada_telefono.grid(row=2,column=1)
entrada_tipo_cb=ttk.Combobox(lblFrame_persona,textvariable=usuario1,font=("Roboto Cn",12),width=15)
entrada_tipo_cb.grid(row=2,column=3)
entrada_tipo_cb["value"]=["Propietario","Arrendatario","Visitante"]

#********************BOTONES DE LA VENTANA DATOS PERSONALES**********************************
imguardar=Image.open("imagenes/guardar.png")
imguardar = imguardar.resize((60, 60), Image.Resampling.LANCZOS)
imguardar=ImageTk.PhotoImage(imguardar)
imgEditar=Image.open("imagenes/editar.png")
imgEditar = imgEditar.resize((60, 60), Image.Resampling.LANCZOS)
imgEditar=ImageTk.PhotoImage(imgEditar)
imgEliminar=Image.open("imagenes/eliminar.png")
imgEliminar = imgEliminar.resize((60, 60), Image.Resampling.LANCZOS)
imgEliminar=ImageTk.PhotoImage(imgEliminar)
imgSalir=Image.open("imagenes/salir.png")
imgSalir = imgSalir.resize((60, 60), Image.Resampling.LANCZOS)
imgSalir=ImageTk.PhotoImage(imgSalir)
imgBuscar=Image.open("imagenes/buscar.png")
imgBuscar = imgBuscar.resize((30, 30), Image.Resampling.LANCZOS)
imgBuscar=ImageTk.PhotoImage(imgBuscar)
boton_guardar_persona=Button(lblFrame_persona_botones, image=imguardar, borderwidth=0,text="Guardar",command=guardarpersona)
boton_guardar_persona.grid(row=0,column=0, padx=30,pady=10)
boton_guardar_persona.config(background="white")
boton_modificar_persona=Button(lblFrame_persona_botones,image=imgEditar, borderwidth=0,text="Modificar",command=editarpersona)
boton_modificar_persona.grid(row=0,column=1, padx=30,pady=10)
boton_modificar_persona.config(background="white")
boton_eliminar_persona=Button(lblFrame_persona_botones,image=imgEliminar, borderwidth=0,text="Eliminar",command=eliminarpersona)
boton_eliminar_persona.grid(row=0,column=2, padx=30,pady=10)
boton_eliminar_persona.config(background="white")
boton_salir_persona=Button(lblFrame_persona_botones,image=imgSalir, borderwidth=0,text="Salir",command=cerrarventanapersonas)
boton_salir_persona.grid(row=0,column=3, padx=20,pady=10)
boton_salir_persona.config(background="white")
boton_validar_persona=Button(lblFrame_persona,image=imgBuscar, borderwidth=0,command=validaridpersona)
boton_validar_persona.place(x=240,y=5)
desactivarlabelyentradaspersona()
#*************************************************************************
#********************* ETIQUETAS DE LA VENTANA  AUTOMOVILES****************************
ventana_autos.title("Registro de Automoviles")
ventana_autos.geometry("500x380")
ventana_autos.resizable(width=False,height=False)
cabezados = Label(ventana_autos,image=imgcabecera)
cabezados.config(background="white")
cabezados.pack()
lblFrame_personauto = LabelFrame(ventana_autos)
lblFrame_personauto.place(x= 10, y= 110, width= 480)
lblFrame_autos = LabelFrame(ventana_autos)
lblFrame_autos.place(x= 10, y= 160, width= 480)
lblFrame_autobotones = LabelFrame(ventana_autos)
lblFrame_autobotones.place(x= 10, y= 280, width= 480)
label_id_p=Label(lblFrame_personauto,text="Cedula", font=("Roboto Cn",12) )
label_id_p.grid(row=0,column=0,pady=5,padx=5)
label_nombre1=Label(lblFrame_personauto,text="Nombres",font=("Roboto Cn",12))
label_nombre1.grid(row=0,column=2,pady=5,padx=10)
label_placa=Label(lblFrame_autos,text="Placa",font=("Roboto Cn",12))
label_placa.grid(row=1,column=0,pady=5,padx=5,sticky="w")
label_marca=Label(lblFrame_autos,text="Marca",font=("Roboto Cn",12))
label_marca.grid(row=2,column=0,pady=5,padx=5,sticky="w")
label_modelo=Label(lblFrame_autos,text="Modelo",font=("Roboto Cn",12))
label_modelo.grid(row=2,column=2,pady=5,padx=5)
label_color=Label(lblFrame_autos,text="Color ",font=("Roboto Cn",12))
label_color.grid(row=4,column=0,pady=5,padx=5,sticky="w")
label_esta=Label(lblFrame_autos,text="Estado ",font=("Roboto Cn",12))
label_esta.grid(row=4,column=2,pady=5,padx=5)


#*********************ENTRADAS DE LA VENTANA AUTOMOVILES********************************
entrada_id_p=ttk.Combobox(lblFrame_personauto,width=13,font=("Roboto Cn",12))
entrada_id_p.grid(row=0,column=1,padx=5)
dato=Persona_D.consultaidpersona()
entrada_id_p["value"]=dato
entrada_id_p.current(0)
entrada_id_p.bind("<<ComboboxSelected>>",ejecutanombre)
entrada_nombress=Entry(lblFrame_personauto,textvariable=texto,width=17,font=("Roboto Cn",12))
entrada_nombress.grid(row=0,column=3)
entrada_placa=Entry(lblFrame_autos,font=("Roboto Cn",12),width=15)
entrada_placa.grid(row=1,column=1,padx=10)

dato2=Marca_D.seleccionar()
entrada_marca=ttk.Combobox(lblFrame_autos,textvariable=marca1,width=13,font=("Roboto Cn",12))
entrada_marca.grid(row=2,column=1,padx=10)
entrada_marca["value"]=dato2
entrada_marca.current(0)
entrada_marca.bind("<<ComboboxSelected>>",ejecutamarca)
entrada_marcados=Entry(lblFrame_autos,textvariable=marcarespuesta)#respuestas

dato3=Modelo_D.seleccionar()
entrada_modelo=ttk.Combobox(lblFrame_autos,textvariable=modelo1,width=16,font=("Roboto Cn",12))
entrada_modelo.grid(row=2,column=3,padx=10)
entrada_modelo["value"]=dato3
entrada_modelo.current(0)
entrada_modelo.bind("<<ComboboxSelected>>",ejecutamodelo)
entrada_modelodos=Entry(lblFrame_autos,textvariable=modelorespuesta)


dato4=Color_D.seleccionar()
entrada_color=ttk.Combobox(lblFrame_autos,textvariable=color1,width=13,font=("Roboto Cn",12))
entrada_color.grid(row=4,column=1)
entrada_color["value"]=dato4
entrada_color.current(0)
entrada_color.bind("<<ComboboxSelected>>",ejecutacolor)
entrada_colordos=Entry(lblFrame_autos,textvariable=colorespuesta)


entrada_estado_auto=ttk.Combobox(lblFrame_autos,textvariable=estado1,width=16,font=("Roboto Cn",12))
entrada_estado_auto.grid(row=4,column=3)
entrada_estado_auto["value"]=["Activo","Inactivo"]

#********************BOTONES DE LA VENTANA AUTOMOVILES**********************************
boton_validar_automovil=Button(lblFrame_autos,image=imgBuscar,borderwidth=0,command=validaplacautomovil)
boton_validar_automovil.grid(row=1,column=2 ,pady=5)
boton_guardar_automovil=Button(lblFrame_autobotones,image=imguardar,borderwidth=0,command=guardarauto)
boton_guardar_automovil.grid(row=5,column=0,pady=10,padx=30)
boton_modificar_automovil=Button(lblFrame_autobotones,image=imgEditar,borderwidth=0,command=editarautos)
boton_modificar_automovil.grid(row=5,column=1,pady=10,padx=30)
boton_eliminar_automovil=Button(lblFrame_autobotones,image=imgEliminar,borderwidth=0,command=eliminarautos)
boton_eliminar_automovil.grid(row=5,column=2,pady=10,padx=30)
boton_salir_automovil=Button(lblFrame_autobotones,image=imgSalir,borderwidth=0,command=cerrarventanautos)
boton_salir_automovil.grid(row=5,column=3,pady=10,padx=20)
desactivarlabelyentradasdelautomovil()
#***********************ETIQUETAS DE LA VENTANA PARQUEADERO**************************
##**********************VENTANA HISTORIAL******************************************
ventana_historial.title("CONJUNTO RESIDENCIAL CATALUÑA")
ventana_historial.geometry("1000x600")
ventana_historial.resizable(width=False,height=False)
lblFrame_parqueadero1_entrada = Label(ventana_historial)
lblFrame_parqueadero1_entrada.place(x=0,y=0)

#*************************************************************************
#                ETIQUETAS DE LA VENTANA MARCA
#*************************************************************************
ventana_marca.title("Registro de Marcas")
ventana_marca.geometry("500x280")
ventana_marca.resizable(width=False,height=False)
cabe = Label(ventana_marca,image=imgcabecera)
cabe.config(background="white")
cabe.pack()
lblFrame_marca = LabelFrame(ventana_marca)
lblFrame_marca.place(x= 10, y= 110, width= 480)
lblFrame_marcabotones = LabelFrame(ventana_marca)
lblFrame_marcabotones.place(x= 10, y= 150, width= 480)
label_marcatres=Label(lblFrame_marca,text="Marca",font=("Roboto Cn",12))
label_marcatres.grid(row=0,column=2,pady=5,padx=100)
#**********************************************************************
#                 ENTRADAS DE LA VENTANA MARCA
#************************************************************************
entrada_marcatres=Entry(lblFrame_marca,width=17,font=("Roboto Cn",12))
entrada_marcatres.grid(row=0,column=3)
#***********************************************************************
#                BOTONES DE LA VENTANA MARCA
#***********************************************************************

boton_guardar_marca=Button(lblFrame_marcabotones,image=imguardar,borderwidth=0,command=guardamarca)
boton_guardar_marca.grid(row=5,column=0,pady=10,padx=30)
boton_modificar_marca=Button(lblFrame_marcabotones,image=imgEditar,borderwidth=0)
boton_modificar_marca.grid(row=5,column=1,pady=10,padx=30)
boton_eliminar_marca=Button(lblFrame_marcabotones,image=imgEliminar,borderwidth=0,)
boton_eliminar_marca.grid(row=5,column=2,pady=10,padx=30)
boton_salir_marca=Button(lblFrame_marcabotones,image=imgSalir,borderwidth=0,command=cerrarventanamarca)
boton_salir_marca.grid(row=5,column=3,pady=10,padx=20)
#************************************************************************

#*************************************************************************
#                ETIQUETAS DE LA VENTANA COLOR
#*************************************************************************
ventana_color.title("Registro de Marcas")
ventana_color.geometry("500x280")
ventana_color.resizable(width=False,height=False)
cabesa = Label(ventana_color,image=imgcabecera)
cabesa.config(background="white")
cabesa.pack()
lblFrame_color = LabelFrame(ventana_color)
lblFrame_color.place(x= 10, y= 110, width= 480)
lblFrame_colorbotones = LabelFrame(ventana_color)
lblFrame_colorbotones.place(x= 10, y= 150, width= 480)
label_colortres=Label(lblFrame_color,text="Color",font=("Roboto Cn",12))
label_colortres.grid(row=0,column=2,pady=5,padx=100)
#**********************************************************************
#                 ENTRADAS DE LA VENTANA COLOR
#************************************************************************
entrada_colortres=Entry(lblFrame_color,width=17,font=("Roboto Cn",12))
entrada_colortres.grid(row=0,column=3)
#***********************************************************************
#                BOTONES DE LA VENTANA COLOR
#***********************************************************************
boton_guardar_color=Button(lblFrame_colorbotones,image=imguardar,borderwidth=0,command=guardacolor)
boton_guardar_color.grid(row=5,column=0,pady=10,padx=30)
boton_modificar_color=Button(lblFrame_colorbotones,image=imgEditar,borderwidth=0)
boton_modificar_color.grid(row=5,column=1,pady=10,padx=30)
boton_eliminar_color=Button(lblFrame_colorbotones,image=imgEliminar,borderwidth=0,)
boton_eliminar_color.grid(row=5,column=2,pady=10,padx=30)
boton_salir_color=Button(lblFrame_colorbotones,image=imgSalir,borderwidth=0,command=cerrarventanacolor)
boton_salir_color.grid(row=5,column=3,pady=10,padx=20)
#*************************************************************************
#                ETIQUETAS DE LA VENTANA COLOR
#*************************************************************************
ventana_modelo.title("Registro de Modelo")
ventana_modelo.geometry("500x280")
ventana_modelo.resizable(width=False,height=False)
cabesass = Label(ventana_modelo,image=imgcabecera)
cabesass.config(background="white")
cabesass.pack()
lblFrame_modelo = LabelFrame(ventana_modelo)
lblFrame_modelo.place(x= 10, y= 110, width= 480)
lblFrame_modelobotones = LabelFrame(ventana_modelo)
lblFrame_modelobotones.place(x= 10, y= 150, width= 480)
label_modelotres=Label(lblFrame_modelo,text="Modelo",font=("Roboto Cn",12))
label_modelotres.grid(row=0,column=2,pady=5,padx=100)
#**********************************************************************
#                 ENTRADAS DE LA VENTANA MODELO
#************************************************************************
entrada_modelotres=Entry(lblFrame_modelo,width=17,font=("Roboto Cn",12))
entrada_modelotres.grid(row=0,column=3)
#***********************************************************************
#                BOTONES DE LA VENTANA MODELO
#***********************************************************************
boton_guardar_modelo=Button(lblFrame_modelobotones,image=imguardar,borderwidth=0,command=guardarmodelo)
boton_guardar_modelo.grid(row=5,column=0,pady=10,padx=30)
boton_modificar_modelo=Button(lblFrame_modelobotones,image=imgEditar,borderwidth=0)
boton_modificar_modelo.grid(row=5,column=1,pady=10,padx=30)
boton_eliminar_modelo=Button(lblFrame_modelobotones,image=imgEliminar,borderwidth=0,)
boton_eliminar_modelo.grid(row=5,column=2,pady=10,padx=30)
boton_salir_modelo=Button(lblFrame_modelobotones,image=imgSalir,borderwidth=0,command=cerrarventanamodelo)
boton_salir_modelo.grid(row=5,column=3,pady=10,padx=20)
ventana_padre.mainloop()