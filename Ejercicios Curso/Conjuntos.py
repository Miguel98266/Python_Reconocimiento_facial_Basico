#Conjuntos
A={1,2,3,4}
B={2,3,5,6}
C={3,4,6,7}

#Comprar conjunto A == B
print("Comprar conjunto (A == B)")
print(A==B)

# A U B  A union con B
print("(A U B)  A union con B")
print(A|B)

# A U C  A union con C
print("(A U C)  A union con C")
print(A|C)

# B U C  B union con C
print("(B U C)  A union con C")
print(B|C)

# A n B A intersecion con B
print("(A n B) A intersecion con B")
print(A&B)

# A n C A intersecion con C
print("(A n C) A intersecion con C")
print(A&C)

# B n C A intersecion con C
print("(B n C) B intersecion con C")
print(B&C)

# A-B A diferencia de B
print("(A-B) A diferencia de B")
print(A-B)

# A-B A diferencia simetrica de B
print("(A^B) A diferencia simetrica B")
print(A^B)