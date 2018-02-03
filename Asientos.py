# Autor: Andrés Reyes Rangel.
# Calcular en número de asientos en un estadio

def calcularPago(numerosBoletosA, numerosBoletosB, numerosBoletosC):
    totalPago = (numerosBoletosA*870)+(numerosBoletosB*650)+(numerosBoletosC*235)
    return totalPago


def main():
    numerosBoletosA = int(input('¿Cuántos boletos de la "clase A" desea comprar?: '))
    numerosBoletosB = int(input('¿Cuántos boletos de la "clase B" desea comprar?: '))
    numerosBoletosC = int(input('¿Cuántos boletos de la "calse C" desea comprar?: '))
    resultado = calcularPago(numerosBoletosA, numerosBoletosB, numerosBoletosC)
    print("El costo total es: $%.2f " % resultado)
main()