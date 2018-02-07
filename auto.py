##Autor: David Medina A01653311
##Calcular rendimiento de un auto

##Esta funcion es para calcular el rendimiento de km/l
def calcularRendimientoKmLitros(km,gas):
    rKm = km/gas
    return rKm

##Esta funcion es para calcular rendimiento de millas/galones
def calcularRendimientoMillasGalones(km,gas):
    m = km / 1.6093
    gal = gas * 0.264
    mG = m/gal
    return mG

##Esta funcion es para calcular gasolina necesaria para recorrer cierta distancia
def calcularGasParaRecorrerKms(km,rendimiento):
    gas = km/rendimiento
    return gas

## funcion principal
def main():
    kmRecorridos = int(input("Ingresar kilometros recorridos: "))
    gas = int(input("Ingresar gasolñina gastada: "))

    rendimientoKmL = calcularRendimientoKmLitros(kmRecorridos,gas)
    rendimientoMG = calcularRendimientoMillasGalones(kmRecorridos, gas)

    print ("El rendimiento del automóvil en kilometros/litros es: %.2f" % rendimientoKmL, "km/l.")
    print ("El rendimiento del automóvil en millas/galones es: %.2f" % rendimientoMG, "mi/ga.")

    kmARecorrer = int(input("Ingresar kilometros a recorrer: "))
    rendimiento = rendimientoKmL
    gasNecesaria = calcularGasParaRecorrerKms(kmARecorrer, rendimiento)

    print ("Para recorrer", kmARecorrer, "km, necesitas %.2f"% gasNecesaria , "litros de gasolina.")

main()
