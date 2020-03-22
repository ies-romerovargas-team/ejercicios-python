#Ejercicio 01.06
print("Números triangulares desde 1 hasta n")
n = int(input("Indique número n: "))

for x in range(1, n + 1):
	print(str(x) + " - " + str(x * (x + 1) / 2))

acumulado = 0
for x in range(1, n + 1):
	acumulado = acumulado + x
	print(str(x) + " - " + str(acumulado))

