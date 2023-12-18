class Apartamento:
    def __init__(self, id_apartamento = None, Bloque = None, numero = None, id_persona = None):
        self.id_apartamento = id_apartamento
        self.bloque = Bloque
        self.numero = numero
        self.id_persona = id_persona

    def get_id_apartamento(self):
        return self.id_apartamento
    
    def set_id_apartamento(self, id_apartamento):
        self.id_apartamento = id_apartamento
    
    def get_Bloque(self):
        return self.Bloque
    
    def set_Bloque(self, Bloque):
        self.Bloque = Bloque
    
    def get_Numero(self):
        return self.numero
    
    def set_Numero(self, numero):
        self.numero = numero
    
    def get_id_persona(self):
        return self.id_persona
    
    def set_id_persona(self, id_persona):
        self.id_persona = id_persona

#Prueba
# if __name__ == '__main__':
#     Apartamento1 = Apartamento()
#     Apartamento1.set_id_apartamento(20)
#     Apartamento1.set_Bloque("B")
#     Apartamento1.set_Numero(201)
#     Apartamento1.set_id_persona(1067958612)
#     print(Apartamento1.get_id_apartamento())
#     print(Apartamento1.get_Bloque())
#     print(Apartamento1.get_Numero())
#     print(Apartamento1.get_id_persona())