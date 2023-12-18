class Funciones:
	
	def limpiarpersona():
		enombre.delete(0,END)
		return enombre
		"""etelefono.delete(0,END)
		eemail.delete(0,END)
		eestado.delete(0,END)
		etipo.delete(0,END)
		enombre.focus_set()"""
	"""

	def guardarpersona():
		a=set(enombre. get())
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
	"""