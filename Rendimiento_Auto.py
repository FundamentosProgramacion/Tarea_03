# Autor: Fernando Sebastian Silva Miramontes
# Calcular el rendimiento de un auto para despues predecir la gasolina requerrida para el camino que se plantea recorrer.

def calculoKmL(kmRecorridos, gasUsada):    # Calcula el rendimiento en Km/L
    return kmRecorridos/gasUsada


def calculoMi_Gal(km_L):   # Pasa el rendimiento de las unidades Km/L a Mi/Gal
    return km_L/0.424776


def calculoGasAUsar(km_L, kmFuturos):        # Calcula cuanta gasolina se utilizara en el trayecto planteado
    return kmFuturos/km_L


def main() :
    kmRecorridos = int(input("Km's recorridos: "))
    gasUsada = int(input("Gasolina utilizada: "))
    km_L = calculoKmL(kmRecorridos, gasUsada)
    mi_gal = calculoMi_Gal(km_L)
    print("Si recorres %ikms con %i litros de gasolina, el rendimiento es:\n%.2f km/l\n%.2f mi/gal" % (kmRecorridos, gasUsada, km_L, mi_gal))
    kmFuturos = int(input("Cuantos km se van recorrer? "))
    gasFutura = calculoGasAUsar(km_L, kmFuturos)
    print("Para recorrer " + str(kmFuturos) + " necesitas %.2f litros de gasolina" % gasFutura)

main()