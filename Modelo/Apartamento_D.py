import sys 
sys.path.append("../Controlador")
from Apartamento import Apartamento 
from conexion import Conexion
import pandas as pd
SELECCIONAR='SELECT * FROM apartamento'
ELIMINAR='DELETE FROM apartamento WHERE id_apartamento=?'
INSERTAR='INSERT INTO  apartamento(id_apartamento,Bloque,numero,id_persona) VALUES(?,?,?,?)'
MODIFICAR="UPDATE apartamento set bloque=? where id_apartamento=?"
class Apartamento_D:
	def insertar(apartamento):
		conexion=Conexion.ObtenerConexion()
		cursor= Conexion.ObtenerCursor(conexion)
		valor=[apartamento.id_apartamento,apartamento.bloque,apartamento.numero,apartamento.id_persona]
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
if __name__=='__main__':
	apartamento=Apartamento(210,5,100,329297958620)
	Apartamento_D.insertar(apartamento)
	#dato=(2,205)
	#Apartamento_D.modificar(dato)
	#dato=(210,)
	#Apartamento_D.eliminar(dato)
	

	#Persona_D.eliminar(dato)
	datoz=Apartamento_D.consultar()

	df=pd.DataFrame(datoz,columns=["ID","Bloque","Numero","Id_persona"])
	print(df)