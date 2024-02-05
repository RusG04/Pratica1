empleados = []

def agregar_empleado():
    nombre = input("Ingrese el nombre del empleado: ")
    cargo = input("Ingrese el cargo del empleado: ")
    empleados.append({"nombre": nombre, "cargo": cargo})
    print(f"Empleado {nombre} agregado con éxito.")

def buscar_cargo_por_nombre():
    nombre = input("Ingrese el nombre del empleado para buscar su cargo: ")
    for empleado in empleados:
        if empleado["nombre"] == nombre:
            print(f"El cargo de {nombre} es: {empleado['cargo']}")
            return
    print(f"No se encontró un empleado con el nombre {nombre}.")

def eliminar_empleado():
    nombre = input("Ingrese el nombre del empleado que desea eliminar: ")
    for empleado in empleados:
        if empleado["nombre"] == nombre:
            empleados.remove(empleado)
            print(f"Empleado {nombre} eliminado con éxito.")
            return
    print(f"No se encontró un empleado con el nombre {nombre}.")

def mostrar_menu():
    print("\nMenú:")
    print("1. Agregar empleado")
    print("2. Buscar cargo por nombre")
    print("3. Eliminar empleado")
    print("4. Salir")

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        agregar_empleado()
    elif opcion == "2":
        buscar_cargo_por_nombre()
    elif opcion == "3":
        eliminar_empleado()
    elif opcion == "4":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intente nuevamente.")

