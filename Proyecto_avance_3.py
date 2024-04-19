# Lista para almacenar las tareas
tareas_hacer = []

# Función para cargar las tareas desde un archivo de texto al iniciar el programa
def cargar_tareas():
    try:
        with open("tareas.txt", "r") as archivo:
            tareas = []
            # Iteramos sobre cada línea del archivo y convertimos los datos a un diccionario
            for linea in archivo:
                datos = linea.strip().split(",")  # Dividimos la línea en campos separados por coma
                tarea = {
                    "titulo": datos[0],
                    "descripcion": datos[1],
                    "fecha": datos[2],
                    "costo": float(datos[3]),
                    "completada": datos[4] == "True"
                }
                tareas.append(tarea)  # Añadimos la tarea a la lista de tareas
        return tareas
    except FileNotFoundError:
        print("El archivo de tareas no existe o no se encontraron datos.")
        return []

# Función para guardar las tareas en un archivo de texto al salir del programa
def guardar_tareas(tareas):
    with open("tareas.txt", "w") as archivo:
        for tarea in tareas:
            archivo.write(f"{tarea['titulo']},{tarea['descripcion']},{tarea['fecha']},{tarea['costo']},{tarea['completada']}\n")

# Cargar las tareas al iniciar el programa
tareas_hacer = cargar_tareas()

#En este paso con un while para que el programa siga ejecutandose mostramos el menu#
while True:
    print("\nMenú Principal:")
    print("1. Agregar Tarea")
    print("2. Ver Tareas Pendientes")
    print("3. Ver Tareas Completadas")
    print("4. Marcar Tarea como Completada")
    print("5. Editar o Borrar Tareas")
    print("6. Mostrar Estadísticas")
    print("0. Salir")
#Solicitamos al usuario la opcion que desee#
    opcion = input("Seleccione una opción: ")
#En esta parte solicitamos al usuario todo lo relacionado a la tarea y tambien las demas opciones con if#
    if opcion == "1":
        titulo = input("Ingrese el nombre de la tarea: ")
        descripcion = input("Ingrese la descripción de la tarea: ")
        fecha = input("Ingrese la fecha de la tarea (opcional): ")
        costo = float(input("Ingrese el costo de la tarea: "))
        tareas_hacer.append({"titulo": titulo, "descripcion": descripcion, "fecha": fecha, "costo": costo, "completada": False})
        print("Tarea agregada exitosamente.")
    elif opcion == "2":
        print("Tareas Pendientes:")
        for i, tarea in enumerate(tareas_hacer):
            if not tarea["completada"]:
                print(f"{i+1}. Título: {tarea['titulo']}, Descripción: {tarea['descripcion']}, Fecha: {tarea['fecha']}, Costo: ${tarea['costo']}")
    elif opcion == "3":
        print("Tareas Completadas:")
        for i, tarea in enumerate(tareas_hacer):
            if tarea["completada"]:
                print(f"{i+1}. Título: {tarea['titulo']}, Descripción: {tarea['descripcion']}, Fecha: {tarea['fecha']}, Costo: ${tarea['costo']}")
    elif opcion == "4":
        num_tarea = int(input("Ingrese el número de la tarea completada: "))
        if 1 <= num_tarea <= len(tareas_hacer):
            tareas_hacer[num_tarea - 1]["completada"] = True
            print("Tarea marcada como completada.")
        else:
            print("Número de tarea inválido.")
    elif opcion == "0":
        # Guardar las tareas al salir del programa
        guardar_tareas(tareas_hacer)
        print("Sesión finalizada correctamente")
        break
    elif opcion == "5":
        opcion_5 = input("¿Desea editar (e) o borrar (b) una tarea? (e/b): ")
        if opcion_5.lower() == "e":
            num_tarea = int(input("Ingrese el número de la tarea que desea editar: "))
            if 1 <= num_tarea <= len(tareas_hacer):
                # Mostramos los detalles de la tarea seleccionada y permitimos editar la descripción
                tarea = tareas_hacer[num_tarea - 1]
                print("Tarea seleccionada:")
                print(f"Título: {tarea['titulo']}, Descripción: {tarea['descripcion']}, Fecha: {tarea['fecha']}, Costo: ${tarea['costo']}, Completada: {tarea['completada']}")
                nueva_descripcion = input("Ingrese la nueva descripción de la tarea: ")
                tarea["descripcion"] = nueva_descripcion
                print("Tarea editada exitosamente.")
            else:
                print("Número de tarea inválido.")
        elif opcion_5.lower() == "b":
            num_tarea = int(input("Ingrese el número de la tarea que desea borrar: "))
            if 1 <= num_tarea <= len(tareas_hacer):
                # Borramos la tarea seleccionada de la lista de tareas
                tarea_borrada = tareas_hacer.pop(num_tarea - 1)
                print(f"Tarea '{tarea_borrada['titulo']}' borrada exitosamente.")
            else:
                print("Número de tarea inválido.")
        else:
            print("Opción inválida.")
    elif opcion == "6":
        total_tareas = len(tareas_hacer)
        total_tareas_pendientes = sum(1 for tarea in tareas_hacer if not tarea["completada"])
        total_tareas_completadas = sum(1 for tarea in tareas_hacer if tarea["completada"])
        total_costo_pendientes = sum(tarea["costo"] for tarea in tareas_hacer if not tarea["completada"])
        total_costo_completadas = sum(tarea["costo"] for tarea in tareas_hacer if tarea["completada"])

        print("\nEstadísticas:")
        print(f"Número total de tareas: {total_tareas}")
        print(f"Número total de tareas pendientes: {total_tareas_pendientes}")
        print(f"Número total de tareas completadas: {total_tareas_completadas}")
        print(f"Total del coste ($) de tareas pendientes: ${total_costo_pendientes:.2f}")
        print(f"Total del coste ($) de tareas completadas: ${total_costo_completadas:.2f}")
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
