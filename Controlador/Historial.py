class Historial:
    def __init__(self, id_historial = None, id_automovil = None,id_camara = None ,fechahora = None):
        self.id_historial = id_historial
        self.id_automovil = id_automovil
        self.id_camara=id_camara
        self.fechahora = fechahora

    def get_id_historial(self):
        return self.id_historial
    
    def set_id_historial(self, id_historial):
        self.id_historial = id_historial

    def get_id_automovil(self):
        return self.id_automovil
    
    def set_id_automovil(self, id_automovil):
        self.id_automovil = id_automovil

    def get_id_camara(self):
        return self.id_camara
    
    def set_id_camara(self, id_camara):
        self.id_camara = id_camara

    def get_fechahora(self):
        return self.fechahora
    
    def set_fechahora(self, fechahora):
        self.fechahora = fechahora

    
#Prueba
# if __name__ == '__main__':
#     Historial1 = Historial()
#     Historial1.set_id_historial(2032)
#     Historial1.set_id_automovil(102)
#     Historial1.set_Fecha("10/05/2023")
#     Historial1.set_Hora("19:30")
#     Historial1.set_EandS("Entrada")
#     print(Historial1.get_id_historial())
#     print(Historial1.get_id_automovil())
#     print(Historial1.get_Fecha())
#     print(Historial1.get_Hora())
#     print(Historial1.get_EandS())