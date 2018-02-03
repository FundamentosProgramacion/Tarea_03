#Autor: Eduardo Roberto Müller Romero
#Calcula el precio de boletos dependiendo de la zona donde se ubican los asientos

def main():
	asientosA = int(input("¿Cuántos boletos compraron en la zona A? "))
	asientosB = int(input("¿Cuántos boletos compraron en la zona B? "))
	asientosC = int(input("¿Cuántos boletos compraron en la zona C? "))
	pago = calcularPago(asientosA, asientosB, asientosC)
	print("Asientos de zona A:", asientosA, "\nAsientos de zona B:", asientosB, "\nAsientos de zona C:", asientosC)
	print("El pago Total es: $%.02f" % pago)

def calcularPago(a, b, c): #Esta función calcula el importe por cada zona y luego suma los cargos para obtener el total
	zonaA = a * 870
	zonaB = b * 650
	zonaC = c * 235
	pagoTotal = zonaA + zonaB + zonaC
	return pagoTotal

main()