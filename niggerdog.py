#Crear 3 tipos de perfiles, para esto se deben realizar: Vendedores, Oficiales de Seguridad y Administrativos

class Person():
    def __init__(self, name, age, country, cellphone, worked_Hours, salary_x_hour):
        self.name = name
        self.age = age
        self.country = country
        self.cellphone = cellphone
        self.worked_Hours = worked_Hours
        self.salary_x_hour = salary_x_hour

    def __str__(self):
        return f"{self.name} has {self.age}, lives in {self.country} and the cellphone is {self.cellphone}. The worked hours are {self.worked_Hours} and the salary per hour is {self.salary_x_hour}"


class Seller(Person):
    def __init__(self, name, age, country, cellphone, worked_Hours, salary_x_hour, turno):
        super().__init__(name, age, country, cellphone, worked_Hours, salary_x_hour)
        self.turno = turno
    def __str__(self):
        return f"{self.name} has {self.age}, lives in {self.country} and the cellphone is {self.cellphone}. The worked hours are {self.worked_Hours} and the salary per hour is {self.salary_x_hour}. The turn of work is {self.turno}"

    def salario_devengado(self, worked_Hours):
        return worked_Hours * self.salary_x_hour

class SegurityOfficial(Person):
    def __init__(self, name, age, country, cellphone, worked_Hours, salary_x_hour, categoria):
        super().__init__(name, age, country, cellphone, worked_Hours, salary_x_hour)
        self.categoria = categoria

    def __str__(self):
        return f"{self.name} has {self.age}, lives in {self.country} and the cellphone is {self.cellphone}. The worked hours are {self.worked_Hours} and the salary per hour is {self.salary_x_hour}, the category is {self.categoria}"

    def salario_devengado(self, worked_Hours):
        return worked_Hours * self.salary_x_hour

class Administrativos(Person):
    def __init__(self, name, age, country, cellphone, worked_Hours, salary_x_hour, grado_academico):
        super().__init__(name, age, country, cellphone, worked_Hours, salary_x_hour)
        self.grado_academico = grado_academico

    def __str__(self):
        return f"{self.name} has {self.age}, lives in {self.country} and the cellphone is {self.cellphone}. The worked hours are {self.worked_Hours} and the salary per hour is {self.salary_x_hour}, the academic grade is {self.grado_academico}"

    def salario_devengado(self, worked_Hours):
        return worked_Hours * self.salary_x_hour


class CameraMan(Person):
    def __init__(self, name, age, country, cellphone, worked_Hours, salary_x_hour, experience):
        super().__init__(name, age, country, cellphone, worked_Hours, salary_x_hour)
        self.experience = experience

    def __str__(self):
        return f"{self.name} has {self.age}, lives in {self.country} and the cellphone is {self.cellphone}. The worked hours are {self.worked_Hours} and the salary per hour is {self.salary_x_hour}. Experienced {self.experience}"

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------->

#Instances
#Seller
seller = Seller("Minor", 50, "Costa Rica", 70124904, 24, 1000000,"Day")
salario1 = seller.salario_devengado(seller.worked_Hours)
# print(f"El salario devengado por {seller.name} es: {salario1}")
# print(salario1)


#Official

oficial = SegurityOfficial("Tony", 50, "Peru", 1234567, 16, 250000,"Guarda 1")
salario2 = oficial.salario_devengado(oficial.worked_Hours)
print(salario2)
#Administrativos

administrative = Administrativos("Hannia", 45, "Costa Rica", 83396311, 24, 1000000, "Doctor")
salario3 = administrative.salario_devengado(administrative.worked_Hours)

# print(salario3)
