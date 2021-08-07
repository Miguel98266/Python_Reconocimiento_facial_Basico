#Ejercicio 2
#Crear un programa que pida 3 numeros y determine cual es mayor

n1=int(input("Ingresa el primer numero: "))
n2=int(input("Ingresa el segundo numero: "))
n3=int(input("Ingresa el tercer numero: "))

if n1>n2 and n1>n3:
    print(f"El numero {n1} es el mayor ")
elif n2>n1 and n2>n3:
    print(f"El numero {n2} es el mayor ")
elif n3>n1 and n3>n2:
    print(f"El numero {n3} es el mayor ")
else:
    print("Los tres numeros son iguales ")