#Ejercicio 01.07
def factorial(n):
	f = 1
	for x in range(1, n + 1):
		f = f * x
	return f

print("Cálculo factorial de m números introducidos por teclado")
n1 = int(input("Número de valores a introducir: "))
valores = []
for x in range(n1):
	n2 = input("Introduzca valor nº " + str(x+1) +": ")
	valores.append(n2)

for element in valores:
	res = factorial(int(element))
	print(str(element) + "! = " + str(res))