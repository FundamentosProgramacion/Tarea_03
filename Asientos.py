# Autor: Guillermo Adrian Urbina Aguiñiga
# Programa para calcular asientos en un estadio

def CalcularAsientos(Asientosa,Asientosb,Asientosc):
    Totalpago = (Asientosa * 870.00) + (Asientosb * 650.00) + (Asientosc * 235.00)
    return Totalpago
# Esta función calcula el total de los boletos

def main():
    AsientosA = int(input("Número de asientos A: "))
    AsientosB = int(input("Número de asientos B: "))
    AsientosC = int(input("Número de asientos C: "))
    Total = CalcularAsientos(AsientosA,AsientosB,AsientosC)
    print("El número de Asientos A es: ", AsientosA)
    print("El número de Asientos B es: ", AsientosB)
    print("El número de Asientos C es: ", AsientosC)
    print("El costo total es: ", Total)
# Esta función resuelve el problema

main()
