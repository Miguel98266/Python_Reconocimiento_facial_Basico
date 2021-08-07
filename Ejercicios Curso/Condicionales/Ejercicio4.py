# Ejercicio 4
# Crear un programa que simule un cajero automatico con un saldo
# inicial de $2000 con el siguiente menu:
# 1-Ingreso de dinero
# 2-Retirar dinero
# 3-Mostrar dinero
# 4-Salir

saldo = 2000
print("1-Ingreso de dinero")
print("2-Retirar dinero")
print("3-Mostrar dinero")
print("Salir")

opcion = int(input("Escribe el numero que desees: "))

if opcion == 1:
    ingreso = int(input("Cuanto vas a depositar: "))
    saldo = saldo + ingreso
    print("Tu  saldo es: ", saldo)
elif opcion == 2:
    retiro = int(input("Cuanto vas a retirar: "))
    if retiro > saldo:
        print("Saldo insuficiente")
    else:
        saldo = saldo - retiro
        print("Tu saldo es: ", saldo)
elif opcion == 3:
    print("Tu saldo es: ", saldo)
elif opcion == 4:
    print("Adios")
else:
    print("Esa opcion no existe")
