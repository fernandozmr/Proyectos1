print ("Ingrese sus datos")

nombre = input("name: \n").upper()
apellido = input ("surname: \n").lower()
age = input("age: \n")
adress = input ("Localidad: \n").upper()
pais = input ("Pais: \n").upper()

print("\nLos datos que usted ha ingresado fueron: \n")
print(f"name: {nombre}, \nsurname: {apellido} \nage: {age} años. \nDe: {adress} \nPais {pais} \n¡¡Bienvenido!!")
