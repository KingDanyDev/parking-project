class Camaras:
    def __init__(self, id_camara = None,id_parqueadero = None ,numero = None, area = None, longitud = None):
        self.id_camara = id_camara
        self.id_parqueadero = id_parqueadero
        self.numero = numero
        self.area = area
        self.longitud = longitud
        
    def get_id_camara(self):
        return self.id_camara
    
    def set_id_camara(self, id_camara):
        self.id_camara = id_camara

    def get_id_parquedero(self):
        return self.id_parqueadero
    
    def set_id_parqueadero(self, id_parqueadero):
        self.id_parqueadero = id_parqueadero

    def get_Numero(self):
        return self.numero
    
    def set_Numero(self, Placa):
        self.numero = numero

    def get_area(self):
        return self.area
    
    def set_area(self, area):
        self.area = area

    def get_longitud(self):
        return self.longitud
    
    def set_longitud(self, longitud):
        self.longitud = longitud
