class Vehiculo:
    def __init__(self, marca, tipoFuel, color, nivelFuel, averiado = False):
        self.marca = marca
        self.tipoFuel = tipoFuel
        self.color = color
        self.nivelFuel = nivelFuel
        self.averiado = averiado
    def __str__(self):
        return self.marca

    def conducir (self, Km):
        if self.averiado == True:
            print("No puedes conducir, que el vehiculo esta averiado")
        elif self.nivelFuel == 0:
            print(f"No tienes {self.tipoFuel}, tienes que repostar")
        elif self.nivelFuel < 2*Km:
            print(f"Tienes {self.nivelFuel} de {self.tipoFuel}, no es suficiente para hacer los {Km}km. Ve a repostar antes.")
        else:
            self.nivelFuel = self.nivelFuel - (2*Km)
            print(f"Estoy conduciendo. Voy a conducir {Km}kms.")
    def llenar_Deposito(self, nivel):
        self.nivelFuel = nivel + self.nivelFuel
        print(f"Tienes {self.nivelFuel} de {self.tipoFuel}")
    def accidente (self, OtroVehiculo):
        print(f"Has tenido un accidente contra {OtroVehiculo}.")
        OtroVehiculo.averiado = True
        self.averiado = True
        print("Necesitas arreglo")
    def arreglar(self):
        self.averiado = False
        print("El vehiculo está arreglado")
        
    
class Camion(Vehiculo):
    def __init__(self, marca, tipoFuel, color, nivelFuel, cabina):
        super(). __init__(marca, tipoFuel, color, nivelFuel)
        self.cabina = cabina
    def dormir (self):
        print("Dejame en paz que estoy dormiendo")

class Moto (Vehiculo):
    def __init__(self, marca, tipoFuel, color, nivelFuel, manillar):
        super(). __init__(marca, tipoFuel, color, nivelFuel)
        self.manillar = manillar
    def hacerCaballito (self):
        print("Soy el p.amo!")

camion1 = Camion("Nissan", "gasolina", "Blanco",200, "grande")
print(camion1.marca)
camion1.llenar_Deposito(100)
camion1.conducir(100)
camion1.conducir(200)

moto1 = Moto("Kymco", "gasoil", "Negro" , 50, "ancho" )
moto1.hacerCaballito()
moto1.accidente(camion1)
camion1.conducir(20)
moto1.conducir(20)
moto1.arreglar()
moto1.conducir(10)