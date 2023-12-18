import sys 
sys.path.append("../Controlador")
from Historial import Historial 
from conexion import Conexion
import pandas as pd
SELECCIONAR='SELECT * FROM historial'
ELIMINAR='DELETE FROM historial WHERE id_historial=?'
INSERTAR='INSERT INTO historial(id_historial, id_automovil, id_camara, fechahora) VALUES(?,?,?,?)'
MODIFICAR="UPDATE historial set fechahora=? where id_historial=?"
class Historial_D:
	def insertar(historial):
		conexion=Conexion.ObtenerConexion()
		cursor= Conexion.ObtenerCursor(conexion)
		valor=[historial.id_historial, historial.id_automovil, 
		historial.id_camara, historial.fechahora]
		cursor.execute(INSERTAR,valor)
		conexion.commit()
		print("el registro se guardó")
		conexion.close()
	def modificar(dato):
		conexion=Conexion.ObtenerConexion()
		cursor= Conexion.ObtenerCursor(conexion)
		cursor.execute(MODIFICAR,dato)
		conexion.commit()
		print("el registro se actualizó")
		conexion.close()	
	def eliminar(dato):
		conexion=Conexion.ObtenerConexion()
		cursor= Conexion.ObtenerCursor(conexion)
		cursor.execute(ELIMINAR,dato)
		conexion.commit()
		print("el registro se eliminó")
		conexion.close()
	def consultar():
		conexion=Conexion.ObtenerConexion()
		cursor= Conexion.ObtenerCursor(conexion)
		cursor.execute(SELECCIONAR)
		dato=cursor.fetchall()
		conexion.commit()
		conexion.close()
		return dato					
if __name__ == '__main__':
	hist=Historial(4,4,42,"12/12/2023")
	Historial_D.insertar(hist)

	#dato=("20/05/1983")
	#Historial_D.modificar(dato)
	#Persona_D.eliminar(dato)
	#dato=(201,)

	#Persona_D.eliminar(dato)
	datoz=Historial_D.consultar()