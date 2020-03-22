#Ejercicio 01.03
def fahrenheitCelsius(gradosF):
    gradosC = (gradosF - 32) / (9 / 5)
    return gradosC

#def celsiusFahrenheit(gradosC):
#    gradosF = (gradosC * 9 / 5) + 32
#    return gradosF

f = int(input('Introduce grados Fahrenheit: '))
print(fahrenheitCelsius(f))