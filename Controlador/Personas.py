class Persona:
    def __init__(self, id_persona = None, nombre = None, telefono = None, email = None, estado = None, tipo = None):
        self.id_persona = id_persona
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.estado = estado
        self.tipo = tipo

    def get_id_persona(self):
        return self.id_persona
    
    def set_id_persona(self, id_persona):
        self.id_persona = id_persona

    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_telefono(self):
        return self.telefono
    
    def set_telefono(self, telefono):
        self.telefono = telefono
    
    def get_email(self):
        return self.email
    
    def set_email(self, email):
        self.email = email
    
    def get_estado(self):
        return self.estado
    
    def set_estado(self, estado):
        self.estado = estado

    def get_tipo(self):
        return self.tipo
    
    def set_tipo(self, tipo):
        self.tipo = tipo
#Prueba
# if __name__ == '__main__': 
#     carlos = Persona()
#     carlos.set_id_persona(2023)
#     carlos.set_nombre(input("ingrese el nombre: "))
#     carlos.set_telefono(input("ingrese el telefono: "))
#     carlos.set_email(input("ingrese su email: "))
#     carlos.set_estado(input("ingrese el estado: "))
#     carlos.set_tipo(input("ingrese el tipo: "))
#     print(carlos.get_id_persona())
#     print(carlos.get_nombre())
#     print(carlos.get_telefono())
#     print(carlos.get_email())
#     print(carlos.get_estado())
#     print(carlos.get_tipo())