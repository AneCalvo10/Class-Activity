class Analista:
    def __init__(self, name, salario, lenguaje):
        self.name = name
        self.lenguaje = lenguaje
        self.salario = salario
    def calcular_salario(self):
        if self.lenguaje == "Finanzas":
            return self.salario*1.3
        else: return self.salario