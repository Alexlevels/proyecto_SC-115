# Lista para almacenar las tareas
tareas_hacer = []
#En este paso con un while para que el programa siga ejecutandose mostramos el menu#
while True:
    print("\nMenú Principal:")
    print("1. Agregar Tarea")
    print("2. Ver Tareas Pendientes")
    print("3. Ver Tareas Completadas")
    print("4. Marcar Tarea como Completada")
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
        print("Sesión finalizada correctamente")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
