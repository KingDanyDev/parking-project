class Parqueadero:
    def __init__(self, id_parqueadero = None, numero = None, totalceldas = None):
        self.id_parqueadero = id_parqueadero
        self.numero = numero
        self.totalceldas = totalceldas
        
    def get_id_parquedero(self):
        return self.id_parqueadero
    
    def set_id_parqueadero(self, id_parqueadero):
        self.id_parqueadero = id_parqueadero
    
    def get_Numero(self):
        return self.numero
    
    def set_Numero(self, Placa):
        self.numero = numero

    def get_totalceldas(self):
        return self.totalceldas
    
    def set_totalceldas(self, totalceldas):
        self.totalceldas = totalceldas
#Prueba
# if __name__ == '__main__':
#     Automovil1 = Automovil()
#     Automovil1.set_id_automovil(201)
#     Automovil1.set_Placa("BHK 065")
#     Automovil1.set_Marca("BMW")
#     Automovil1.set_Modelo(2024)
#     Automovil1.set_Color("Dorado")
#     Automovil1.set_Estado("Activo")
#     Automovil1.set_id_persona(1067958612)
#     print(Automovil1.get_id_automovil())
#     print(Automovil1.get_Placa())
#     print(Automovil1.get_Marca())
#     print(Automovil1.get_Modelo())
#     print(Automovil1.get_Color())
#     print(Automovil1.get_Estado())
#     print(Automovil1.get_id_persona())
