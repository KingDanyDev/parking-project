import sys 
sys.path.append("../Controlador")
from Automovil import Automovil 
from conexion import Conexion
import pandas as pd
SELECCIONAR='SELECT * FROM auto'
ELIMINAR='DELETE FROM auto WHERE id_automovil=?'
INSERTAR='INSERT INTO  auto(id_automovil,placa,marca,modelo,color,estado,id_persona) VALUES(?,?,?,?,?,?,?)'
MODIFICAR="UPDATE auto set marca=? where placa=?"

class Automovil_D:
	def insertar(auto):
		conexion=Conexion.ObtenerConexion()
		cursor= Conexion.ObtenerCursor(conexion)
		valor=[auto.id_automovil,auto.placa,auto.marca,auto.modelo,auto.color,auto.estado,auto.id_persona]
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
if __name__ == '__main__':
	auto=Automovil(2,"AKL451","Mercedes",2023,"Rojo","Activo",200)
	Automovil_D.insertar(auto)
	#dato=("dolores",201)
	#Persona_D.modificar(dato)
	#Persona_D.eliminar(dato)
	#dato=(201,)

	#Persona_D.eliminar(dato)
	datoz=Automovil_D.consultar()
	df=pd.DataFrame(datoz,columns=["id_automovil","Placa","Marca","Modelo","Color","Estado","id_persona"])
	print(df)
	