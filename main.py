import os

tareas = []

ruta_archivo = os.path.join("..", "data", "tareas.txt")

def cargar_tareas():
    if os.path.exists("ruta_archivo"):
        with open("ruta_archivo", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                partes = linea.strip().split("||")
                if len(partes) == 2:
                    texto, estado = partes
                    completada = True if estado == "hecha" else False
                    tareas.append({"texto": texto, "completada": completada})
        print("Tareas cargadas desde tareas.txt")
    else:
        print("No se encontró el archivo tareas.txt. Se iniciará con una lista vacía.")

def mostrar_menu():
    print("\n--- ORGANIZADOR DE TAREAS ---")
    print("1. Agregar nueva tarea")
    print("2. Ver tareas pendientes")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Guardar y salir")

def agregar_tarea():
    tarea = input("Escribe la nueva tarea: ")
    tareas.append({"texto": tarea, "completada": False})
    print("Tarea agregada con éxito.")

def ver_tareas():
    if not tareas:
        print("No hay tareas aún.")
    else:
        print("\n--- TAREAS ---")
        for i, tarea in enumerate(tareas):
            estado = "✔" if tarea["completada"] else "❌"
            print(f"{i + 1}. {tarea['texto']} [{estado}]")

def completar_tarea():
    ver_tareas()
    try:
        num = int(input("¿Qué tarea completaste? (número): "))
        if 0 < num <= len(tareas):
            tareas[num - 1]["completada"] = True
            print("¡Tarea marcada como completada!")
        else:
            print("Número de tarea inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número.")

def eliminar_tarea():
    ver_tareas()
    try:
        num = int(input("¿Qué tarea quieres eliminar? (número): "))
        if 0 < num <= len(tareas):
            tareas.pop(num - 1)
            guardar_tareas()           
            print("Tarea eliminada y guardada correctamente.")
        else:
            print("Número de tarea inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número.")

def guardar_tareas():
    with open("ruta_archivo", "w", encoding="utf-8") as archivo:
        for tarea in tareas:
            estado = "hecha" if tarea["completada"] else "pendiente"
            linea = f"{tarea['texto']}||{estado}\n"
            archivo.write(linea)
    print("Tareas guardadas en el archivo tareas.txt")

def ejecutar():
    cargar_tareas()
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            ver_tareas()
        elif opcion == "3":
            completar_tarea()
        elif opcion == "4":
            eliminar_tarea()
        elif opcion == "5":
            guardar_tareas()
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida, intenta otra vez.")

if __name__ == "__main__":
    ejecutar()
