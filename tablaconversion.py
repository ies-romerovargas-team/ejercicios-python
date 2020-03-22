#Ejercicio 01.04
def fahrenheitCelsius(gradosF):
    gradosC = (gradosF - 32) / (9 / 5)
    return gradosC

for x in range(0, 120, 10):
	print(str(x) + " - " + str(round(fahrenheitCelsius(x),2)))