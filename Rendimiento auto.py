# encoding: UTF-8
#Autor: Genaro Ortiz Durán
#Descripción:Crear programa que calcule el rendimiento de un auto.
milla=1.6093
galon = 0.264

# Convierte los kilometros a millas y los litros a galones. Para calcular el rendimiento se dividen las millas sobre los galones.
def calcularRendimientoMillasGalon(milla,galon,distancia,gasto):
    kmamilla = distancia / milla
    litroagalon = gasto * galon
    rendimientomigal = kmamilla / litroagalon

    return rendimientomigal
#Se calcula elrendimiento dividiendo la distancia sobre el gasto(litros).
def calcularRendimiento(distancia, gasto):
    rendimiento=distancia/gasto


    return rendimiento


def main():
    distancia=int(input("Teclea los kilometros recorridos:"))
    gasto=int(input("Teclea los litros usados:"))

    print("El rendimiento al recorrer",distancia,"km con 17 litros es:",format(calcularRendimiento(distancia,gasto),".2f"),"km/l")
    print("El rendimiento al recorrer",distancia,"km con 17 litros es:",format(calcularRendimientoMillasGalon ( milla, galon, distancia, gasto ), ".2f" ), "mi/gal" )

    distancia1=int(input("¿Cuántos kilometros vas a recorrer?:"))
    litrosrequeridos= distancia1/calcularRendimiento(distancia,gasto)
    print("Para recorrer",distancia1,"km necesitas",format(litrosrequeridos,".2f"),"litros de gasolina")

main()