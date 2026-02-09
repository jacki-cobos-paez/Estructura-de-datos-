#ejercicio 1
lado = float (input("ingrese la longitud del lado del cuadrado: "))
area = lado ** 2

print (f" la superficie del cuadrado es: {area}")

#ejercicio 2
num1 = 10
num2 = 5
suma = num1 + num2
resta = num1 - num2
multi = num1 * num2
divi = num1 / num2
print("suma", suma)
print("resta", resta)
print("multi", multi)
print("divi", divi)

#ejercicio 3
numero = 5
print("valor inicial:", numero)

numero += 1
print("despues de incrementar:", numero)

numero -= 1
print("despues de decrementar:", numero)

#ejercicio 4
cadena1= " aprendiendo"
cadena2= "pyton"

concatenacion = cadena1 + " " + cadena2
print(concatenacion)

#ejercicio 5
valor1= True
valor2= False

and_logico = valor1 and valor2
or_logico = valor1 or valor2
not_logico = not valor1

print("and:", and_logico)
print("or:", or_logico)
print("not:", not_logico)

#ejercicio 6
a = 5.6
b = 2.3

redondeo_a = round(a)
redondeo_b = round(b,1)

potencia = a ** b

print("valor de a:", a)
print("valor de b:", b)
print("redondeo de a:", redondeo_a)
print("redondeo de b (1 decimal):", redondeo_b)
print("a elevado a b:", potencia)

#ejercicio 7
lista1= [1, 2, 3]
lista2= [4, 5]

concatenacion = lista1 + lista2

repeticion = lista1 * 3

print("lista1:", lista1)
print("lista2:", lista2)
print("concatenacion:", concatenacion)
print("repeticion:", repeticion)

#ejercicio 8
numero = 10

print(numero == 10)
print(numero > 7)
print(numero < 20)

#ejercicio 9
a = 17
b = 5


division_entera = a // b

modulo = a % b

print("División entera:", division_entera)
print("Módulo:", modulo)

#ejercicio 10
tupla1 = (1, 2, 3)
tupla2 = (4, 5)


tupla_concatenada = tupla1 + tupla2
a
tupla_repetida = tupla1 * 3

print("Tupla 1:", tupla1)
print("Tupla 2:", tupla2)
print("Tupla concatenada:", tupla_concatenada)

#ejercicio 11
entero = 10
flotante = 3.5
texto = "5"

suma = entero + flotante
resta = entero - flotante
multiplicacion = entero * flotante
division = entero / flotante

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)

#ejercicio 12
suma_convertida = entero + int(texto)
multiplicacion_convertida = flotante * int(texto)

print("Suma con texto convertido:", suma_convertida)
print("Multiplicación con texto convertido:", multiplicacion_convertida)
