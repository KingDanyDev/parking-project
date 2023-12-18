import sqlite3
class Conexion:
	def ObtenerConexion(conexion=None):
		conexion=sqlite3.connect('PARQUEADERO.db')
		return conexion
	def ObtenerCursor(conexion):
		cursor=conexion.cursor()
		return cursor
