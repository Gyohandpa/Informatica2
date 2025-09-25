"""Clase"""
class carro():
    #Definicion de funciones para declarar los valores de la clase(que poseeran cada uno de los objetos)
    def __init__ (self):
        self.capacidad=5
        self.color="Morado"
        self.numLlantas=8
    def avanzar(self,k):
        print(f"Avanzó {k} Km")
""" Objetos """
k1=carro()
k2=carro()
k3=carro()
k2.color="Amarillo"
print(k2.color)

""" Clases de ejercicios """
class celulares():
    def __init__(self):
        self.nombre="Oppo"
        self.dimensiones=14
        self.procesador="snapdragon"
        self.camara=48
    def tomarFoto(self,nombre,k):
        print(f"El telefono {nombre} ha tomado {k} fotos")
class personaje():
    def __init__(self):
        self.nombre="Barbaro"
        self.tipo="Guerrero"
        self.colorPelo="Castaño"
        self.salud=200
        self.dañoFisico=15
        self.velocidad=10
    def verNombre(self,nombre):
        print(f"El nombre del personaje es {nombre}")
    def verTipo(self,tipo):
        print(f"Su tipo es {tipo}")
