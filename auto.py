#encoding: UTF-8
#Jean Paul Esquivel Lobato
#Calcula el rendimiento de un automovil

#Función para realizar la conversión de millas por litros
def calcularMillasXLitros(km, litros):
    return km/litros

#Función para realizar la conversión de galones por millas
def calcularGalonXMillas(km, litros):
    millas = km / 1.6093
    galones = litros * .264
    rendimiento = millas / galones
    return rendimiento

#Función principal
def main():
    kmRecorridos = int(input("Teclea el número de km recorridos: "))
    gasolina = int(input("Teclea el número de km litros de gasolina usados: "))
    kilometrosALitros =calcularMillasXLitros(kmRecorridos, gasolina)
    millasAGalon = calcularGalonXMillas(kmRecorridos, gasolina)
    print(" ")
    print("Si recorres %d kms con %.0f litros de gasolina, el rendimeinto es de:" % (kmRecorridos, gasolina))
    print("%.2f" % kilometrosALitros, ("km/l"))
    print("%.2f" % millasAGalon, ("mi/gal"))

    kmRec = int(input("¿Cuántos kilómetros vas a recorrer? "))
    litrosNecesarios = kmRec / kilometrosALitros
    print("Para recorrer %d km. necesitas %.2f litros de gasolina""" % (kmRec, litrosNecesarios))


#Llama a la función main
main()
