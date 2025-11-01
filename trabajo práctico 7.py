#Ejercicio 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

#Ejercicio 2
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

#Ejercicio 3
lista_frutas = list(precios_frutas.keys())
print(lista_frutas)

#Ejercicio 4
contactos = {}

for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número: ")
    contactos[nombre] = numero

consulta = input("Ingrese un nombre para buscar su número: ")
print("Número:", contactos.get(consulta, "No encontrado"))

#Ejercicio 5
frase = input("Ingrese una frase: ")
palabras = frase.split()

unicas = set(palabras)
frecuencia = {}

for palabra in palabras:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

print("Palabras únicas:", unicas)
print("Recuento:", frecuencia)

#Ejercicio 6
alumnos = {}

for i in range(3):
    nombre = input("Nombre del alumno: ")
    notas = input("Ingrese 3 notas separadas por coma: ")
    tupla_notas = tuple(map(float, notas.split(',')))
    alumnos[nombre] = tupla_notas

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: promedio = {promedio}")

#Ejercicio 7
parcial1 = {"Sofía", "Luis", "Camila", "Diego"}
parcial2 = {"Camila", "Diego", "Julieta", "Tomás"}
ambos = parcial1 & parcial2
print("Aprobaron ambos parciales:", ambos)

solo_uno = parcial1 ^ parcial2
print("Aprobaron solo uno:", solo_uno)

al_menos_uno = parcial1 | parcial2
print("Aprobaron al menos un parcial:", al_menos_uno)

#Ejercicio 8
stock = {}

while True:
    producto = input("Nombre del producto (o 'salir'): ")
    if producto.lower() == 'salir':
        break
    if producto in stock:
        cantidad = int(input("Cantidad a agregar: "))
        stock[producto] += cantidad
    else:
        cantidad = int(input("Cantidad inicial: "))
        stock[producto] = cantidad

consulta = input("Consultar stock de: ")
print("Stock:", stock.get(consulta, "Producto no encontrado"))

#Ejercicio 9
agenda = {}

while True:
    dia = input("Día (o 'salir'): ")
    if dia.lower() == 'salir':
        break
    hora = input("Hora: ")
    evento = input("Evento: ")
    agenda[(dia, hora)] = evento

consulta_dia = input("Consultar día: ")
consulta_hora = input("Consultar hora: ")
print("Evento:", agenda.get((consulta_dia, consulta_hora), "No hay evento"))

#Ejercicio 10
original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
invertido = {capital: pais for pais, capital in original.items()}

print("Original:", original)
print("Invertido:", invertido)

#FIN