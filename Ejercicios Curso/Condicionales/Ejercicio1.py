
#Ejercicio 1
#Crear un programa que pida 2 numeros y obtenga como resultado
#cual de ellos es par o si ambos lo son

n1=int(input("Escribe un numero: "))
n2=int(input("Ingrese otro numero: "))

if (n1%2==0) and (n2%2==0):
    print("Ambos son pares")
elif (n1%2==0) and (n2%2!=0):
    print(f"El numero {n1} es par")
elif (n1%2!=0) and (n2%2==0):
    print(f"El numero {n2} es par")
else:
    print("Los dos son impares")