
## Importar las clases de programador y anlaista
import Programador as P
import Analista as A

#Crear la clase para calcular las nominas
class Sistema_Nominas:
    #parametro -  una lista de clase Empleado
    def calcular_nominas(self, empleados):
        print("Calculando nominas")
        for empleado in empleados:
            print(f"Nomina para : {empleado.name} - {empleado.lenguaje} ")
            print(f"{empleado.calcular_salario()} € ")
            
    
##Caracteristicas de los empleados y crear una lista con ellos
empleado1 = P.Programador("Jon", 30000, "Python")
empleado2 = P.Programador("Marta", 30000, "Java")
empleado3= P.Programador("Leo", 30000, "HTML")
empleado4 =A.Analista("Jon", 40000, "Finanzas") 

empleados = (empleado1, empleado2, empleado3,empleado4)

#Ejecutar el metodo para calcular los salarios
nominas = Sistema_Nominas()
nominas.calcular_nominas(empleados)