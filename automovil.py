#Ricardo Cornejo Lozano
#Calcula el rendimiento de un automovil en km/l, mi/gal y la gasolina necesaria para recorrer el kilometraje deseado.

def renKm():
    totalKm = km/lts
    return (totalKm)

def renMi():
    totalMi = km/1.6093
    totalL = lts*0.264
    return (totalMi/totalL)

def main():
    global km
    global lts
    km = int(input("Teclea el numero de km recorridos: "))
    lts = int(input("Teclea el numero de litros de gasolina uasdos: "))
    total = renMi()
    total2 =renKm()
    print ("Si recorres", str(km), "kms con " +str(lts), "litros de gasolina, el rendimiento es: ", "\n %.2f km/l" %(total), "\n %.2f mi/g" %(total2))
    calcularNes = int(input("\n¿Cuantos Kilometros vas a recorrer? "))
    calculo = (calcularNes / total2)
    print ("\nPara recorrer " +str(calcularNes), "km. necesitas %.2f" %(calculo), "litros de gasolina.")

main()

