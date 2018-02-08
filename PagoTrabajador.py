# Autor: Carlos Martínez Rodríguez
# Descripción: Calcular pago de trabajador con horas extras

# Función que calcula el pago normal por horas de trabajo
def calcularPagoNormal(horasNormales, pagoHora):
    total = horasNormales * pagoHora
    return total
# Función que calcula el pago por horas extras tomando en cuenta el porcentaje extra de 75%
def calcularPAgoExtra(horasExtras, pagoHora):
    total = horasExtras * (pagoHora * 1.75)
    return total

def main():
    # Entradas del usuario
    horasNormales = int(input("Teclea las horas normales trabajadas: "))
    horasExtras = int(input("Teclea las horas extras trabajadas: "))
    pagoHora = int(input("Teclea el pago por hora: "))
    # Calcular pago de horas normales, extras y el total de ambas
    totalHorasN = calcularPagoNormal(horasNormales, pagoHora)
    totalHorasE = calcularPAgoExtra(horasExtras, pagoHora)
    totalPago = totalHorasN + totalHorasE
    # Imprimir
    print("Pago normal: $%.02f" % totalHorasN)
    print("Pago extra: $%.02f" % totalHorasE)
    print("---------------")
    print("Total: $%.02f" % totalPago)

main()