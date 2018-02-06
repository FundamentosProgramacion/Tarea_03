#Autor: Jorge Mora Cárdenas
#Calcula el rendimiento de los coches según la gasolina utilizada y los km recorridos.

def calcularRendimiento (kilometros, gasolina):
    #Calcula el rendimiento en km/l
    division = kilometros / gasolina
    return division

def conversionMillas(kilometros, gasolina):
    # convierte todas las unidades al sistema inglés y da calcula el rendimiento.
    convertirMillas = kilometros * 1.6093
    convertirGalon = gasolina * 0.264
    rendimiento = convertirMillas / convertirGalon
    return rendimiento

def calcularGasolina (Kmrecorrer,Kilometros, gasolina):
    #Calcula el total de litros que se necesitarán para recorrrer “x” numero de kilometros
    litros = (Kmrecorrer * gasolina)/ Kilometros
    return litros



def main():
    Km = int(input("Teclea el numero de kilometros recorridos: "))
    Gasolina = int(input("Teclea los litros de gasolina utilizados: "))
    rendimiento = calcularRendimiento (Km, Gasolina)
    millas = conversionMillas(Km,Gasolina)

    print("Si recorres", Km," kms con ",Gasolina," litros de gasolina, recorreras: ")
    print("%.2f"%rendimiento," km/l")
    print("%.2f"%millas," mi/gal")

    kmRecorrer = int(input("¿Cuantos Kilometros vas a recorrer? "))
    recorrido = calcularGasolina(kmRecorrer, Km, Gasolina)
    print("Para recorrer",kmRecorrer,"se necesitan %.2f"%recorrido," L de gasolina")

main()
