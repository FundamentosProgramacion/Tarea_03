#Autor: Nataly Paulina Lopez Salazar
#Descripcion: Calcular el rendimiento de un coche con base a los km y litros de gasolina y los litros que va necesiar en cierta distancia.

def calcularRend(km, lit): #Esta funcion calcula el rendimiento con los km y litros.
    r = km/lit
    return r

def calcularConv(km, lit): #Esta funcion hace las conversiones de km a millas y de litros a galones.
    millas = km/1.6093
    gal = lit*0.264
    conversion = millas/gal
    return conversion


def calcularLitros(kilo, km, lit): #Esta funcion calcula los litros que se van usar con respecto a otra distancia.
    litros = (kilo*lit)/km
    return litros


def main():
    km = int(input("Numero de km recorridos: "))
    lit = int(input("Litros de gasolina usados: "))
    print("\nSi recorres %i kms con %i litros de gasolina, el rendimiento es:"%(km,lit))

    rend = calcularRend(km,lit)
    conv = calcularConv(km,lit)

    print("%.2f km/l"%rend)
    print("%.2f mi/gal"%conv)

    kilo = int(input("¿Cuántos kilometros vas a recorrer? "))
    gas = calcularLitros(kilo,km,lit)

    print("Para recorrer %i km. necesitas %.2f litros de gasolina."%(kilo,gas))

main()