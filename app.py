from Llave import Key
from Helado import Ice_Cream

print("Llave.")
size = input("Ingrese el tamaño de la llave: ")

colour = input("Ingrese el color de la llave: ")

my_key = Key(size, colour)

print(my_key)

print("---------------------")

print("Helado.")
colour = input("Ingrese el color del helado: ")

flavour = input("Ingrese el sabor del helado: ")

my_ice_cream = Ice_Cream(colour, flavour)

print(my_ice_cream)

