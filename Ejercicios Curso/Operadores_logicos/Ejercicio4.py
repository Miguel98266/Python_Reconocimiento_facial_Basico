#Ejercicio 4
#Obtener el precio final que se tiene que pagar
#si se aplica el 36% de descuento del total de la 
#compra.

precio=float(input("Ingrese el precio: "))
descuento=(precio*36)/100
preciofinal=precio-descuento

print(f"El precio final es: {preciofinal}")