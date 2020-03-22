#Ejercicio 01.01
# Escribir un ciclo definido para imprimir por pantalla todos los números entre 10 y 20

for x in range(10, 21):
	print(x)
print("")

# Escribir un ciclo definido que salude por pantalla a sus cinco mejores amigos/as

amigo=["Sara", "Juan", "Carmen", "Marina", "Sebastián"]
for x in range(5):
	print("Hola, " + amigo[x])
print("")

# Escribir un programa que use un ciclo definido con rango numérico, que pregunte los nombres de sus cinco mejores amigos/as, y los salude.

for x in range(5):
	a = input("Nombre de amigo/a " + str(x) + ": ")
	print("Hola, " + a)
print("")

# Escribir un programa que use un ciclo definido con rango numérico, que pregunte los nombres de sus seis mejores amigos/as, y los salude.

for x in range(6):
	a = input("Nombre de amigo/a " + str(x) + ": ")
	print("Hola, " + a)
print("")

# Escribir un programa que use un ciclo definido con rango numérico, que averigue a cuántos amigos quieren saludar, les pregunte los nombres de esos amigos/as, y los salude.

n = input("¿Cuántos amigos tiene? ")
for x in range(n):
	a = input("Nombre de su amigo/a n° " + str(x) + ": ")
	print("Hola, " + a)
print("")