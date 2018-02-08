#Ricardo Cornejo Lozano
#Calcula el pago de un trabajador conforme a sus horas de trabajo.

def hnormal(horas):
    total =(pago*horas)
    return total

def hextra(horas2):
    adicional = (pago*.75)
    total1 = ((adicional+pago)*horas2)
    return total1

def main():
    global pago
    horas = int(input("Teclea las horas normales trabajadas: "))
    horas2 = int(input("Teclea las horas extras trabajadas: "))
    pago = int(input ("Teclea el pago por hora: "))
    total = hnormal(horas)
    total1 = hextra(horas2)
    print ("\nPago normal: $%.2f " % +(total), "\nPago extra: $%.2f " % total1, "\n_____________________", "\nPago total: $%.2f " % (total +total1))

main()
    
    

