#Ejercicio 01.05
print("Números pares entre dos números")
n1 = int(input("Indique número 1: "))
n2 = int(input("Indique número 2: "))
mayor = n1
menor = n2
if n2 > n1:
	mayor = n2
	menor = n1
if menor%2!=0:
	menor = menor +1
for x in range(menor,mayor,2):
	print(x)