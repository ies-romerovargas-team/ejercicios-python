#Ejercicio 01.02
C = int(input("Capital inicial: "))
x = float(input("Tipo anual: "))
n = int(input("Años: "))
res = C * (1 + x / 100) ** n
print(round(res,2))