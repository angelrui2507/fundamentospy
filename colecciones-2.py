# Tuplas
# (item, item2, itemN)
# Inmutables
my_tuple = ("uno", 2, 3.1, False)
print(type(my_tuple))
print(my_tuple [0])
print(my_tuple[-1])
# Error
# my_tuple[0] = "nuevo Valor"

# Conjutos Set
# {item1, item2, itemN}
# Colecciones sin indice y sin duplicados

my_set = {1, 2, 2, 2, 3, 4, "uno"}
print(type (my_set))
print(my_set)
my_set.add(5)

a = {1, 2, 3, 4}
b = {4, 5, 6, 7}
print(a.union (b))
print(a.intersection(b))
print(a.difference(b))

# Diccionarios
# { item1: valor, item2: valor }

alumno = {
    "name": "shaggy",
    "lname": "lugo",
    "age": 20,
    "genre": "M",
    "calificaciones": [9, 9, 9]
}
print(type (alumno))
print(alumno)
print(alumno["name"], alumno ["lname"])
if alumno["age"] < 20:
    print("Es menor de edad")
alumno["calificaciones"].append(10)
print(alumno ["calificaciones"])   