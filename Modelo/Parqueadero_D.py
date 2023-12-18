import sys 
sys.path.append("../Controlador")
from Parqueadero import Parqueadero 
from conexion import Conexion
import pandas as pd
SELECCIONAR='SELECT * FROM Parqueadero'
ELIMINAR='DELETE FROM Parqueadero WHERE id_parqueadero=?'
INSERTAR='INSERT INTO  Parqueadero(id_parqueadero,numero,totalceldas) VALUES(?,?,?)'
MODIFICAR="UPDATE Parqueadero set totalceldas=? where id_parqueadero=?"
class Parqueadero_D:
	def INSERTAR(parqueadero):
		conexion=Conexion.ObtenerConexion()
		cursor= Conexion.ObtenerCursor(conexion)
		valor=[parqueadero.id_parqueadero,parqueadero.numero,parqueadero.totalceldas]
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
	#parq1=Parqueadero(2,5,29)
	#Parqueadero_D.INSERTAR(parq1)

	#dato=(100,3)
	#Parqueadero_D.MODIFICAR(dato)

	#dato=(3,)
	#Parqueadero_D.ELIMINAR(dato)


	datoz=Parqueadero_D.consultar()
	df=pd.DataFrame(datoz,columns=["ID Parqueadero","Numero de Celdas","Total de Celdas"])
	print(df)