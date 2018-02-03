#Autor: Eduardo Roberto Müller Romero
# Este programa calcula el pago que se le tiene que dar a un trabajador usano como entrada las horas regulares y extras que este laboró

def main():
	sueldo = float(input("¿Cuánto cobra por hora? "))
	horas_Regulares =  int(input("¿Cuántas horas a la semana trabaja? "))
	horas_Extra = int(input("¿Cuántas horas extra trabajó? "))
	pago_Normal = calcularPagoR(sueldo, horas_Regulares)
	pago_Extra = calcularPagoE(sueldo, horas_Extra)
	total_aPagar = pago_Normal + pago_Extra
	print("Pago Normal: $%.02f" % pago_Normal, "\nPago Extra: $%.02f" % pago_Extra, "\nSueldo Total: $%.02f" % total_aPagar)

def calcularPagoR(sueldo, horas):#La función calcula el pago regular
	sueldo_fijo = horas * sueldo
	return sueldo_fijo

def calcularPagoE(sueldo, horasExtra): #La función calcula el sueldo por cada hora extra y lo multiplica por el número de horas
	sueldoExtra = sueldo * 1.75
	pago_Extra = sueldoExtra * horasExtra
	return pago_Extra

main()