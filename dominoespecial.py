#Ejercicio 01.09
n = int(input("Indique el número de puntos que puede contener la ficha: "))
for f1 in range(1, n + 2):
	for f2 in range(1, f1 + 1):
		print(str(f1 - 1) + "/" + str(f2 - 1))