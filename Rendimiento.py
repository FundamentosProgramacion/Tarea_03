#Autor: Karla Fabiola Ramirez Martinez
#Calcula el rendmiento de un auto



def calcularkml(km,gasolina):
    rendimiento=km/gasolina
    return rendimiento


def calcularmig(km,gasolina):
    millas=km/1.6093
    galones=0.264*gasolina
    rendimientro=millas/galones
    return rendimientro

def respuestalitros(pregunta,kml):
    respuesta=pregunta/kml
    return respuesta
def main():
    km=int(input("Teclea el numero de kilometros recorridos: "))
    gasolina=int(input("Teclea el numero de litros de gasolina usados: "))
    kml=calcularkml(km,gasolina)
    miga=calcularmig(km,gasolina)
    print("Si recorres ",km," kms con ",gasolina," litros de gasolina, el rendimiento es: ")
    print("%.2f"%kml,"km/l")
    print("%.2f"%miga,"mi/gal")
    pregunta=int(input("¿Cuantos kilometros vas a recorrer? "))
    litrosrespuesta=respuestalitros(pregunta,kml)
    print("Para recorrer ",pregunta," km. necesitas %.2f"%litrosrespuesta," litros de gasolina")







main()