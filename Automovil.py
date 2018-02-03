#Autor: Eduardo Roberto Müller Romero
'''
Este programa recibe los km que recorre un auto con cierto número de litros de gasolina, devuelve el rendimiento de este
para posteriormente decirle al usuario cuantos litros de gasolina necesita para viajar el número de km que este desea viajar
'''

def main():
	km_Recorridos = float(input("¿Cuántos km has recorrido? "))
	litrosUsados = float(input("¿Cuántos litros has gastado? "))
	rendimientoenKm, rendimientoenMi = calcularelRendimiento(km_Recorridos, litrosUsados)
	print("Si recorres", km_Recorridos, "kms con", litrosUsados, "litros de gasolina, el rendimiento de tu vehículo es:\n%.02f" % rendimientoenKm, "km/l\n%.02f" % rendimientoenMi, "mi/gal\n")
	kmaRecorrer = float(input("¿Cuántos km vas a recorrer? "))
	litrosNecesarios = calcularLitros(rendimientoenKm, kmaRecorrer)
	print("Para recorrer", kmaRecorrer, "km,  %.02f" % litrosNecesarios, "litros de gasolina serán necesarios")

def calcularelRendimiento(km, litros):
	rendimientokm = km / litros
	convertirMi = km  / 1.6093
	convertirGal = litros * .264
	rendimientomigal = convertirMi / convertirGal
	return rendimientokm, rendimientomigal

def calcularLitros(rendimiento, km):
	litros = km / rendimiento
	return litros

main()