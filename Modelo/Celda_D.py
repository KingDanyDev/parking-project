import sys 
sys.path.append("../Controlador")
from Celda import Celda 
from conexion import Conexion
import pandas as pd
SELECCIONAR='SELECT * FROM celda'
ELIMINAR='DELETE FROM celda WHERE id_celda=?'
INSERTAR='INSERT INTO  celda(id_celda,id_apartamento,id_parqueadero,numerocelda) VALUES(?,?,?,?)'
MODIFICAR="UPDATE celda set numerocelda=? where id_celda=?"

class Celda_D:
	def INSERTAR(celda):
		conexion=Conexion.ObtenerConexion()
		cursor= Conexion.ObtenerCursor(conexion)
		valor=[celda.id_celda,celda.id_apartamento,celda.id_parqueadero,celda.numerocelda]
		cursor.execute(INSERTAR,valor)
		conexion.commit()
		print("el registro se guardo")
		conexion.close()
	def MODIFICAR(dato):
		conexion=Conexion.ObtenerConexion()
		cursor= Conexion.ObtenerCursor(conexion)
		cursor.execute(MODIFICAR,dato)
		conexion.commit()
		print("el registro se actualizo")
		conexion.close()
	def ELIMINAR(dato):
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
if __name__ == '__main__':
	#celda1=Celda(3,2,2,8)
	#Celda_D.INSERTAR(celda1)
	#dato=(2,1)
	#Celda_D.MODIFICAR(dato)

	#dato=(3,)
	#Celda_D.ELIMINAR(dato)



	datoz=Celda_D.consultar()
	df=pd.DataFrame(datoz,columns=["ID Celda","ID Apartamento","ID Parqueadero","Numero de Celdas"])
	print(df)