drinks = []

def add_drink(drink):
    drinks.append(drink)

def del_drink(drink):
    try:
        drinks.remove(drink)
    except Exception:
        print("No existe en la lista")
    
def show_drinks():
    print("-" * 4, "my Drinks", "-" * 4)
    for drink in drinks:
        print("-->", drink)   

choice_text = '''
Elige una Opcion:
    1 - agregar
    2 - eliminar
    3 - mostar
    4 - salir
'''

while True:
    choice_user = int(input (choice_text))
    if choice_user == 1:
        drink = input('Ingresa una bebida: ')
        add_drink(drink)
    elif choice_user == 2:
        drink = input('Ingresa una bebida')
        del_drink(drink)
    elif choice_user == 3:
        show_drinks()
    elif choice_user == 4:
        break
    else:
        print('Opcion Incorrecta')           


