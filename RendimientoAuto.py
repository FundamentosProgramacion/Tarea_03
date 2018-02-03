# Autor: Andrés Reyes Rangel.
# Calcular el rendimiento de un auto.

def calcularKM(kmRecorridos, litrosUsados):
    km= kmRecorridos/litrosUsados
    return km

def calcularMI(kmRecorridos, litrosUsados):
    millas= kmRecorridos/1.6063
    litros = litrosUsados*0.264
    mi= millas/litros
    return mi

def calcularLitros(kmPorRecorrer, rendimientoKM):
    li=kmPorRecorrer/rendimientoKM
    return li

def main():
    kmRecorridos = int(input("Teclea el número de km recorridos: "))
    litrosUsados= int(input("Teclea el número de litros de gasolina usados: "))
    rendimientoKM = calcularKM(kmRecorridos,litrosUsados)
    rendimientoMI = calcularMI(kmRecorridos,litrosUsados)
    print("")
    print("Si recorres %d kms con %d litros de gasolina, el rendimiento es: " % (kmRecorridos,litrosUsados))
    print("%.2f km/l" % rendimientoKM)
    print("%.2f mi/gal" % rendimientoMI)
    print("")
    kmPorRecorrer = int(input("¿Cuántos kilometros vas a recorrer? "))
    litrosNecesarios = calcularLitros(kmPorRecorrer, rendimientoKM)
    print("")
    print("Para recorrer %d km. necesitas %.2f litros de gasolina" % (kmPorRecorrer, litrosNecesarios))
main()