class Automovil:
    def __init__(self, id_automovil = None, placa = None, marca = None, modelo = None, color = None, estado = None, id_persona = None):
        self.id_automovil = id_automovil
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.estado = estado
        self.id_persona = id_persona

    def get_id_automovil(self):
        return self.id_automovil
    
    def set_id_automovil(self, id_automovil):
        self.id_automovil = id_automovil
    
    def get_Placa(self):
        return self.placa
    
    def set_Placa(self, placa):
        self.placa = placa

    def get_Marca(self):
        return self.marca
    
    def set_Marca(self, marca):
        self.marca = marca

    def get_Modelo(self):
        return self.modelo
    
    def set_Modelo(self, modelo):
        self.modelo = modelo

    def get_Color(self):
        return self.color
    
    def set_Color(self, color):
        self.color = color

    def get_Estado(self):
        return self.estado
    
    def set_Estado(self, estado):
        self.estado = estado

    def get_id_persona(self):
        return self.id_persona
    
    def set_id_persona(self, id_persona):
        self.id_persona = id_persona
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
