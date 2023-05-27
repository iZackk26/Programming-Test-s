class Person():
    def __init__(self,name, gender, age, profession, salary):
        self.name = name
        self.gender = gender
        self.age = age
        self.profession = profession
        self.salary = salary
    def __str__(self):
        return f"Nombre: {self.name}, Gender: {self.gender}, Age: {self.age}, Profession: {self.profession}, Salary: {self.salary}"

class Seller(Person):
    """ Inheritance of Person"""
    super().__init__(name, gender, age, profession, salary, categoria)
    def earned_salary(self,worked_hours):
        return worked_hours * self.salary



class Oficial(Person):
    def __init__(self, name, gender, age, profession, salary, categoria):
        super().__init__(name, gender, age, profession, salary, categoria)
        self.categoria = categoria

    def __str__(self):
        return f"Nombre: {self.name}, Gender: {self.gender}, Age: {self.age}, Profession: {self.profession}, Salary: {self.salary}, Category: {self.turn}"



class Administrador(Person):
    def __init__(self, name, gender, age, profession, salary, grado_academico):
        super().__init__(name, gender, age, profession, salary)
        self.grado_academico = grado_academico

    def __str__(self):
        return f"Nombre: {self.name}, Gender: {self.gender}, Age: {self.age}, Profession: {self.profession}, Salary: {self.salary}, Academic Grade: {self.grado_academico}"

class Guarda(Person):
    def __init__(self, name, gender, age, profession, salary, shift):
        super().__init__(name, gender, age, profession, salary)
        self.shift = shift
    
    def patrol(self):
        print(f"El guardia {self.name} está haciendo su recorrido en el turno de {self.shift}")

# Using the Classes referenced before:

seller = Seller("Juanito", "Male", 18,"Seller", 20000,"Licenciado")
print(seller)
oficial = Oficial("Mario", "Male", 20, "Oficial", 1000, "Night")
print(oficial)
administrador = Administrador("Karen", "Female", 22, "Sales Administrador", 350000, "Master")
print(administrador)
guarda = Guarda("Elon Musk", "Male", 19, "CEO of SpaceX and Tesla", "+9999999999")
print(guarda)
