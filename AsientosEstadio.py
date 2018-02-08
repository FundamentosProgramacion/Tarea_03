# Autor: Carlos Martínez Rodríguez
# Descripción: Calcula el precio por cantidad de boletos y tipo de asiento

# Función para calcular el totla de pago dependiendo de la cantidad y tipo de asiento
def calcularPago(asientosA, asientosB, asientosC):
    asA = asientosA * 870
    asB = asientosB * 650
    asC = asientosC * 235
    totalPago = asA + asB + asC
    return totalPago

def main():
    # Entradas del usuario
    numeroBoletosA = int(input("Número de Boletos de la Clase A: "))
    numeroBoletosB = int(input("Número de Boletos de la Clase B: "))
    numeroBoletosC = int(input("Número de Boletos de la Clase C: "))
    # Calcular el costo total por el númeor y tipo de asientos
    total = calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC)
    # Imprimir resultados
    print("El costo total es: $%.2f" % total)

main()