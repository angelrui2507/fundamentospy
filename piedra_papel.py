# Eleccion aleatoria maq
import random

# function randint(min-max)
rand_int = random.randint(1, 3)
if rand_int ==1:
    choice_maq = 'piedra'
elif rand_int == 2:
    choice_maq = 'papel'
else:
    choice_maq = 'tijeras'
            
# Eleccion de usuario
choice_text = '''
escribe una de las operaciones:
    piedra
    papel
    tijeras
'''
choice_user = input(choice_text)
# Impresion de Operaciones
print('usuario eligio ->', choice_user)
print('maquina elegio ->', choice_maq)

# Ganador!
if choice_maq == choice_user:
    print("Es unj empate")
else:
    if choice_maq == 'piedra' and choice_user == 'papel':
        print('gana usuario!')
    elif choice_maq == 'piedra' and choice_user == 'tijeras':
        print('gana maquina!')
    elif choice_maq == 'papel' and choice_user == 'tijeras':
        print('gana usuario!')
    elif choice_maq == 'papel' and choice_user == 'piedra':
        print('ganana maquina!') 
    elif choice_maq == 'tijeras' and choice_user == 'piedra':
        print('gana usuario!')
    else:
        print('gana maquina!')                     