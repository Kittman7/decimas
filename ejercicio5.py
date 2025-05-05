#Biblioteca digital

biblioteca = ["libro1", "libro2", "libro3", "libro4", "libro5"]

print("Biblioteca Digital")
print("1. Ver todos los libros")
print("2. Buscar un libro")
print("3. Agregar un libro")
print("4. Eliminar un libro")

opcion = float(input("\nSeleccione una opción (1-4): "))


if opcion == 1:
    if len(biblioteca) == 0:
        print("La biblioteca está vacía.")
    else:
        print("\nLibros disponibles:")
        for i, libro in enumerate(biblioteca, 1):
            print(f"{i}. {libro}")

elif opcion == 2:
    busqueda = input("Ingrese el nombre del libro a buscar: ")
    encontrado = False
    for libro in biblioteca:
        if busqueda in libro:
            print(f"Libro encontrado: {libro}")
            encontrado = True
    if not encontrado:
        print("No se encontró ningún libro con ese nombre.")

elif opcion == 3:
    nuevo_libro = input("Ingrese el nombre del nuevo libro: ")
    biblioteca.append(nuevo_libro)
    print(f"'{nuevo_libro}' ha sido agregado a la biblioteca.")

elif opcion == 4:
    print("Saliendo del programa.")

else:
    print("Opción no válida. Por favor, elija una opción entre 1 y 4.")