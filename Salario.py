# encoding: UTF-8
#Autor: Genaro Ortiz Durán
#Descripción:Crear programa que calcule el salario de un trabajador.




#Calcula el pago de las horas normales multiplicando la cantidad de horas por el pago por hora.
def calcularPagoNormal(horasNormales, pago):
    normal=horasNormales*pago

    return normal

#Multiplica el resultado de la multiplicación de las horas extras por el pago por hora por 0.75 y le suma la multiplicación de las horas extras por el pago por hora.
def calcularPagoExtra(horasExtras, pago):
    extra=(pago*horasExtras)*0.75+(pago*horasExtras)

    return extra


def main():
    horasNormales = float(input("Teclea las horas normales trabajadas:"))
    horasExtras = float(input("Teclea las horas extras trabajadas:"))
    pago = float(input("Teclea el pago por hora:"))
    print("Pago normal es:","$",format(calcularPagoNormal(horasNormales,pago),".2f"))
    print("Pago extra es:","$",format(calcularPagoExtra(horasExtras,pago),".2f"))


main()
