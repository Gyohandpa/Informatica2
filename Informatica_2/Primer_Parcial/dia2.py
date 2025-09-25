#Tipado dinamico todo lo que es establecer valores a las variables, generando objetos de almacenamiento
#POO es un paradigma que permite a traves de las clases establecer 
#Las ventajas mas grandes son la depuracion de VSCode para la correccion de errores

#La programación orientada a objetos (POO) es un paradigma de programación que organiza el código alrededor de objetos, en lugar de funciones y lógica. Su objetivo principal es facilitar la creación de software modular, reutilizable y fácil de mantener, modelando el mundo real a través de objetos con sus propios datos (atributos) y comportamientos (métodos)

""" def suma(a,b):
    return a + b
a = int(input("Ingrese el Primer numero: "))
v = int(input("Ingrese el Segundo numero: "))

j= suma(a,v)
print(j)
b=['a','b','c','d','e']
c=[{'1': b}, {'key2': 'value2'}, {'key3': 'value3'}]
type(c.get('1')) """
#_______________________________________________________________________________

class Persona:
    especie = "Homosapiens"
    """init inicializa todos los atributos del objeto, es el constructor de la clase"""
    def __init__(self):
        self.nombre = "Juan"
        self.edad = 30
        self.cc=123
    
    def saltar (self,nombre,metros):
        print(f"{nombre} saltó {metros} metros")
    
    """def __str__(self):   le dice a la clase como reaccionar ante un print"""
    def __str__(self):
        return (f"El nombre de esta persona es: {self.nombre}")

f=[]
for i in range(11):
    g= Persona()
    f.append(g)
print(type(f[2]))
#La palabra Self, permite identificar el propio objero que esta ejecutandose, de entre todos los que pueden existir en la memoria en un momento dado

class ave:
    def __init__(self,tipo,vuela):
        self.ave= tipo
        self.vuelo= vuela
        self.oviparos = True
        self.pico = True
    def comer(self,comida):
        print(f"La {self.ave} come {comida}")
    def volar(self):
        print("Este tipo de abe puede volar: ", self.vuelo)
class ganso(ave):
    def __init__(self,tipo,vuela,accion,pata):
        ave.__init__(self,tipo,vuela)
        self.habilidad = accion
        self.pata = pata
    def destreza(self):
        print("Esta ave puede : ", self.habilidad)

class pato(ganso):
    def __init__(self,tipo,vuela,accion,pata):
        ganso.__init__(self,tipo,vuela,accion,pata)
        self.tamaño = "Mediano"
    def pescar(self,tipoPico):
        print(f"El pato puede pescar con su pico {tipoPico}")

class gallina(ave):
    def __init__(self, tipo, vuela, accion):
        ave.__init__(self, tipo, vuela)
        self.habilidad = accion
        self.vuela = False
    def ponerHuevo(self):
        print("La gallina ha puesto un huevo.")
    def huir(self):
        print("La gallina ha huido")

pato1 = pato("Omnivoro",True, "pescar", "Palmeado")
print(pato1.pescar("Ancho"))