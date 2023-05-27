import pickle
class Marciano:

    def __init__(self, name, planet, color):
        self.name = name
        self.planet = planet
        self.color = color

    def __str__(self):
        return f"El marciano {self.name}, viene del planeta {self.planet} y soy del color {self.color}"

    def saludar(self):
        return f"hola soy {self.name}"

    def soy_del_planeta(self):
        return f"Hola vengo del planeta"

class MarcianoAgresivo(Marciano):
    def __init__(self, name, planet, color, arma, balas):
        super().__init__(name, planet, color)
        self.balas = balas

    def marciano_atacar(self):
        return f"El marciano {self.name} de color {self.color} del planeta {self.planet} va atacar con el arma {self.arma}, con una cantida de balas de {self.balas}"
    
class MarcianoInteligente(Marciano):
    def __init__(self, name, planet, color, invento, iq):
        super().__init__(name, planet, color)
        self.invento = invento
        self.iq = iq
    
    def crear(self):
        return f"El marciano {self.nombre} del planeta {self.planeta}, ha creado el invento {self.invento}"
    
    def marciano_iq(self):
        return f"EL marciano {self.nombre} tiene un iq de {self.iq} el cual es mayor al resto de marcianos"

def ma_saved():
    first = MarcianoAgresivo("Joaquin", "Saturno", "Cafe", "Pistola 47", 86)
    second = MarcianoAgresivo("Pedro", "Jupiter", "ROsado", "A mano", 1)

    with open("ma.bin","wb") as file:
        pickle.dump([first, second], file)

    with open("ma.bin","rb") as file:
        x = (pickle.load(file))
        return x


def adding_instance(lista):
    first = MarcianoAgresivo("Joacoo", "Tieraa", "Morado", "AK 47", 240)
    lista.append(first)
    # for element in m_agresive:
    #     print(element)
    return lista


def bubble(lista):
    # -------------------------------
    pasadas = len(lista) - 1
    while pasadas > 0:
        vueltas = 0
        while vueltas < pasadas:
            if lista[vueltas].name > lista[vueltas + 1].name:
                lista[vueltas], lista[vueltas + 1] = lista[vueltas + 1], lista[vueltas]
            vueltas += 1
        pasadas -= 1
    return lista
print(bubble(adding_instance(ma_saved())))



