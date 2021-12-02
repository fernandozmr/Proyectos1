
# N = int(input('Ingrese un N: '))
# suma = 0
# c = 0

# while c <= N:
#     suma = suma + c
#     #print (suma ,'\n')
#     c = c+1

# print(suma)

nombre = input("Ingresa un nombre para agregar a la lista: \n")
lista = []

while nombre != ' ':
    lista.append(nombre)
    nombre = input("Ingresa un nombre para agregar a la lista: \n")

print ("Las personas ingresadas son:")
for i in lista:
    print (i.upper())

print("\n")

