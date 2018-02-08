# Autor: Carlos Martínez Rodríguez
# Descripción: Calcular el rendimiento de un auto con el número de km recorridos y los litros de gasolina gastados

# Función para convertir km a millas
def convertMillas(km):
    millas = km / 1.6093
    return millas

# Función para convertir litros a galones
def convertGalon(gas):
    galon = gas * 0.264
    return galon

# Función para calcular el rendimeinto del coche tomando en cuenta el tipo de unidad internacional o ingles
def calcularRendimiento(km, gas, tipoMedida):
    if (tipoMedida == 'internacional'):
        rendimiento = km / gas
    elif (tipoMedida == 'ingles'):
        rendimiento = convertMillas(km) / convertGalon(gas)
    else:
        rendimiento = 0
    return rendimiento

def main():
    # Entradas del usuario
    kmRecorridos = int(input("Teclea el número de km recorridos: "))
    litrosGasolina = int(input("Teclea el número de litros de gasolina usados: "))
    print("Si recorres %i kms con %i litros de gasolina, el rendimiento es:" % (kmRecorridos, litrosGasolina))

    # Calcular el rendimiento utilizando la función calcularRendimiento
    rendimientoInt = calcularRendimiento(kmRecorridos, litrosGasolina, 'internacional')
    rendimientoIng = calcularRendimiento(kmRecorridos, litrosGasolina, 'ingles')
    # Imprimir resulatados de rendimiento en unidades internacionales e inglesas
    print("%.2f km/l" % rendimientoInt)
    print("%.2f mi/gal" % rendimientoIng)

    # Calcular consumo de gasolina según el rendimeinto previo del coche
    kmDeViaje = int(input("¿Cuántos kilómetros vas a recorrer? "))
    proyeccionKm = kmDeViaje / rendimientoInt
    # Imprimir consumo
    print("Para recorrer %.0f km. necesitas %.2f litros de gasolina" % (kmDeViaje, proyeccionKm))


main()