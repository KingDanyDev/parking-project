
import sys 
sys.path.append("../Controlador")
from conexion import Conexion
from Personas import Persona 
import pandas as pd
SELECCIONAR='SELECT * FROM persona'
ELIMINAR='DELETE FROM persona WHERE id_persona=?'
INSERTAR='INSERT INTO  persona(nombre,telefono,email,estado,tipo) VALUES(null,?,?,?,?,?)'
MODIFICAR="UPDATE persona set nombre=? where id_persona=?"

class Persona_D:
	def insertar(persona):
		conexion=Conexion.ObtenerConexion()
		cursor= Conexion.ObtenerCursor(conexion)
		valor=[persona.nombre,persona.telefono,persona.email,persona.estado,persona.tipo]
		cursor.execute(INSERTAR,valor)
		conexion.commit()
		print("el registro se guardo")
		conexion.close()
	def modificar(dato):
		conexion=Conexion.ObtenerConexion()
		cursor= Conexion.ObtenerCursor(conexion)
		cursor.execute(MODIFICAR,dato)
		conexion.commit()
		print("el registro se actualizo")
		conexion.close()	
	def eliminar(dato):
		conexion=Conexion.ObtenerConexion()
		cursor= Conexion.ObtenerCursor(conexion)
		cursor.execute(ELIMINAR,dato)
		conexion.commit()
		print("el registro se ELIMINO")
		conexion.close()
	def consultar():
		conexion=Conexion.ObtenerConexion()
		cursor= Conexion.ObtenerCursor(conexion)
		cursor.execute(SELECCIONAR)
		dato=cursor.fetchall()
		conexion.commit()
		conexion.close()
		return dato					
#if __name__ == '__main__':
#	pass 
	#persona=Persona(203,"maria",7845214,"picapiedra@gmail.com",0,"propietario")
	#Persona_D.insertar(persona)
	#dato=(201,)
	#Persona_D.modificar(dato)
	#Persona_D.eliminar(dato)
	#dato=(201,)

	#Persona_D.eliminar(dato)
	#datoz=Persona_D.consultar()

	#df=pd.DataFrame(datoz,columns=["ID","Nombre","Telefono","Email","Estado","Tipo"])
	#print(df)
	#print("ID   Nombre  Telefono    Email            Estado      Tipo")
	#for i in datoz:
	#print(f"{i[0]}\t {i[1]}\t {i[2]}\t {i[3]}\t{i[4]}\t{i[5]}")