# Ejercicio 3
# Crear un programa que compare dos nombres,
# y verificar si hay coincidencias o no, si es que
# ambos nombres comienzan con la misma letra
# o si terminan con la misma letra

nombre1 = input("Escribe el primer nombre: ")
nombre2 = input("Escribe el segundo nombre: ")

if nombre1 == nombre2:
    print("Nombre repetido")

elif nombre1[0] == nombre2[0] and nombre1[-1] == nombre2[-1]:
    print("Si hay concidencia con la primera y ultima letra")
else:
    print("No hay coincidencias")
