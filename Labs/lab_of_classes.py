import pickle

class Marciano():
    def __init__(self, nombre, planeta, color):
        self.nombre = nombre
        self.planeta = planeta
        self.color = color

    def saludar(self):
        return f"Hola soy {self.nombre}!"

    def soy_del_planeta(self):
        return f"Hola vengo del planeta {self.planeta}"

    def marciano_color(self):
        return f"El marciano {self.name}, es de color {self.color}"

class Marciano_Agresivo(Marciano):
    def __init__(self, nombre, planeta, color, arma, habilidad):
        super().__init__(nombre, planeta, color)
        self.arma = arma
        self.habilidad = habilidad

    def marciano_atacar(self):
        return f"El marciano {self.nombre}, del planeta {self.planeta} va a atacar con un {self.arma}"

    def marciano_habilidad(self):
        return f"El marciano {self.nombre} tiene una super habilidad con una rareza extrema, su habilidad es {self.habilidad}"

class Marciano_Inteligente(Marciano):
    def __init__(self, nombre, planeta, color, invento, iq ):
        super().__init__(nombre, planeta, color)
        self.invento = invento
        self.iq = iq

    def crear(self):
        return f"El marciano {self.nombre} del planeta {self.planeta}, ha creado el invento {self.invento}"

    def marciano_iq(self):
        return f"EL marciano {self.nombre} tiene un iq de {self.iq} el cual es mayor al resto de marcianos"
def marciano_agre():
    marciano_agre1 = Marciano_Agresivo("XAE-12", "Marte", "Negro", "Arma de Plasma", "Super Salto")
    marciano_agre2 = Marciano_Agresivo("ET", "Marte", "Cafe", "Rayo lazer", "Invisibilidad")
    
    with open("archivo_binario_MarcianoAgresivo.bin","wb") as file:
        pickle.dump([marciano_agre1, marciano_agre2],file)

    with open("archivo_binario_MarcianoAgresivo.bin","rb") as file:
        x = pickle.load(file)
        return x
# marciano_agre()

def marciani_inteli():
    marciano_inte1 = Marciano_Inteligente("Manolo","Jupiter","Azul","Cohete Espacial",99)
    marciano_inte2 = Marciano_Inteligente("Carlito","Saturno","Morado","Cohete Telequinetico",65)
    marciano_inte3 = Marciano_Inteligente("Sebas","Neptuno","Negro","Cohete Espacial",28)

    with open("archivo_binario_MarcianoInteligente.bin","wb") as file:
        pickle.dump([marciano_inte1, marciano_inte2, marciano_inte3],file)

    with open("archivo_binario_MarcianoInteligente.bin","rb") as file:
        x = pickle.load(file)
        return x
# marciani_inteli()

# Cargar Agresivo y agregar dos instancias
def inteli(marciano):
    for alien in marciano:
        print(f"Nombre : {alien.nombre}, Planeta: {alien.planeta}, Color: {alien.color}, Invento: {alien.invento}, IQ: {alien.iq}")

with open("archivo_binario_MarcianoInteligente.bin","rb") as file:
    x = pickle.load(file)
    inteli(x)


with open("arc.bin","rb") as file:
    x = pickle.load(file)
    return x

