# Forma 1: Con el condicional para validar
def forma_1():
    for numero in range(1, 21):
        if numero % 2 == 0:
            print(f"El número {numero} es par.")

# Forma 2: Sin el condicional para válidar. El range se encarga
def forma_2():
    for numero in range(2, 21, 2):
        print(f"El número {numero} es par.")

# Forma 3: Usando while
def forma_3():
    contador = 0
    numero = 1
    while contador < 10:
        if numero % 2 == 0:
            print(f"El número {numero} es par.")
            contador += 1
        numero += 1

# Forma 4: Usando list comprehension
def forma_4():
    pares = [num for num in range(1, 21) if num % 2 == 0]
    for par in pares:
        print(f"El número {par} es par.")

opciones = {
    "1": forma_1,
    "2": forma_2,
    "3": forma_3,
    "4": forma_4,
    "salir": lambda: print("Saliendo...")
}

if __name__ == "__main__":
    opcion = ""
    while opcion != "salir":
        print("Selecciona una forma de imprimir los primeros 10 números pares:")
        print("1. Con condicional")
        print("2. Sin condicional (usando step en range)")
        print("3. Usando while")
        print("4. Usando list comprehension")
        print("Escribe 'salir' para terminar.")

        opcion = input("Ingrese una opción: ")

        if opcion in opciones:
            opciones[opcion]()
        else:
            print("Opción no válida.")