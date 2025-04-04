estudiantes = {
    "Martin Ferrari": {"edad": 16, "materias": ["Matemáticas", "Lengua"]},
    "Laura Muñoz": {"edad": 15, "materias": ["Biologia", "Historia"]},
    "Angel Hidalgo": {"edad": 17, "materias": ["Matematica", "Frances"]}
}

def agregar():
    nombre = input("Introduce el nombre del estudiante: ")
    edad = int(input("Introduce la edad del estudiante: "))
    materias = input("Introduce las materias aprobadas (separadas por coma): ").split(",")
    estudiantes[nombre] = {"edad": edad, "materias": [materia.strip() for materia in materias]}
    print(f"Estudiante {nombre} agregado exitosamente.")

def mostrar():
    if estudiantes:
        for nombre, info in estudiantes.items():
            print(f"Nombre: {nombre}, Edad: {info['edad']}, Materias: {', '.join(info['materias'])}")
    else:
        print("No hay estudiantes en la lista.")

def eliminar():
    nombre = input("Introduce el nombre del estudiante a eliminar: ")
    if nombre in estudiantes:
        del estudiantes[nombre]
        print(f"Estudiante {nombre} eliminado exitosamente.")
    else:
        print(f"No se encontró un estudiante con el nombre {nombre}.")

def buscar():
    nombre = input("Introduce el nombre del estudiante a buscar: ")
    if nombre in estudiantes:
        info = estudiantes[nombre]
        print(f"Estudiante: {nombre}, Edad: {info['edad']}, Materias: {', '.join(info['materias'])}")
    else:
        print(f"No se encontró un estudiante con el nombre {nombre}.")

def buscarPalabra():
    palabra = input("Introduce una palabra para buscar en los nombres: ")
    encontrados = [nombre for nombre in estudiantes if palabra.lower() in nombre.lower()]
    if encontrados:
        print("Estudiantes encontrados: ", ", ".join(encontrados))
    else:
        print(f"No se encontraron estudiantes con la palabra '{palabra}' en su nombre.")

opcion = -1
while opcion != 6:
    print("\nMenú de opciones:")
    print("1. Agregar estudiante")
    print("2. Mostrar lista de estudiantes")
    print("3. Eliminar estudiante")
    print("4. Buscar estudiante por nombre")
    print("5. Buscar estudiantes por palabra en el nombre")
    print("6. Salir")
    
    opcion = int(input("Ingresa la opción elegida: "))
    
    match opcion:
        case 1:
            agregar()
        case 2:
            mostrar()
        case 3:
            eliminar()
        case 4:
            buscar()
        case 5:
            buscarPalabra()
        case 6:
            print("Saliendo del programa.")
        case _:
            print("Opción no válida. Por favor, elige una opción entre 1 y 6.")