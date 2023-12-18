import sys 
sys.path.append("../Controlador")
from Camaras import Camaras 
from conexion import Conexion
import pandas as pd
SELECCIONAR='SELECT * FROM Camaras'
ELIMINAR='DELETE FROM Camaras WHERE id_camara=?'
INSERTAR='INSERT INTO  Camaras(id_camara,id_parqueadero,numero,area,longitud) VALUES(?,?,?,?,?)'
MODIFICAR="UPDATE Camaras set numero=?, area=?, longitud=? where id_camara=?"

class Camaras_D:
	def INSERTAR(Camaras):
		conexion=Conexion.ObtenerConexion()
		cursor= Conexion.ObtenerCursor(conexion)
		valor=[Camaras.id_camara,Camaras.id_parqueadero,Camaras.numero,Camaras.area,Camaras.longitud]
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
	#Cam1=Camaras(2,5,9,93,56)
	#Camaras_D.INSERTAR(Cam1)

	#dato=(100,50,25,1)
	#Camaras_D.MODIFICAR(dato)

	dato=(2,)
	Camaras_D.ELIMINAR(dato)


	datoz=Camaras_D.consultar()
	df=pd.DataFrame(datoz,columns=["ID Camaras","ID Parqueadero","Numero","Area","Longitud"])
	print(df)