class Programador:
    def __init__(self, name, salario, lenguaje):
        self.name = name
        self.lenguaje = lenguaje
        self.salario = salario
    def calcular_salario(self):
        if self.lenguaje == "Python":
            return self.salario*1.3
        elif self.lenguaje == "Java":
            return self.salario*1.4
        elif self.lenguaje == "HTML":
            return self.salario*1.5
        else: return self.salario