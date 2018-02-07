# encoding: UTF-8
# Sebastian Morales Martin
# Calculo de gasolina


def calcularKmPorLitro(distancia, gas):
    rendimiento = distancia/gas
    return rendimiento

def calcularMiPorGalon(distancia, gas):

    rendimiento = (distancia * 1.6093) / (gas * 0.264)
    return rendimiento

def calcularDistanciaParaGasolina(rendimiento, distancia):
    gas = distancia / rendimiento
    return gas



def main():
    kilometros = float(input("Teclea el número de km recorridos: ")) #evaluado en "float" en caso de que el usuario decida poner decimales
    litros = float(input("Teclea el número de litros de gasolina usados: ")) #evaluado con "float" para que el usuario pueda usar decimales si es que lo necesita
    kmPorLitro = calcularKmPorLitro(kilometros, litros)
    miPorGalon = calcularMiPorGalon(kilometros, litros)
    print("\nSi recorres %d kms con %d litros de gasolina, el rendimiento es:\n"
          "%.2f km/l\n"
          "%.2fmi/gal\n"
          % (kilometros, litros, kmPorLitro, miPorGalon))
    recorrer = float(input("¿Cuántos kilómetros vas a recorrer? "))
    gasolinaNecesaria = calcularDistanciaParaGasolina(kmPorLitro, recorrer)
    print("\nPara recorrer %d km. necesitas %.2f litros de gasolina" % (recorrer, gasolinaNecesaria))


main()
