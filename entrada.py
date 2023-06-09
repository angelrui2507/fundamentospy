# function input -> retorna string

num_a = int(input("Ingresa un numero: "))
num_b = int(input("Ingresa un numero: "))

print(num_a + num_b)

name = input("Ingresa tu nombre:")
age = int(input("ingresa tu edad:"))
city = input("Ingrese tu ciudad /pueblo:")

# string format
"""
hola, soy name, tengo age años y vivo en city
"""
greeting = "hola, soy {}, tengo {}  años y vivo en {}"

print(greeting.format(name, age, city))

greeting_2 = f"hola, soy { name }, tengo { age} años y vivo en { city}"

print(greeting_2)
