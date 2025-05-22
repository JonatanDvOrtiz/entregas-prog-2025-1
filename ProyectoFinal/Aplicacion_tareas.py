"""
Título de práctica: Aplicacion_tareas

Sistema para organizar tareas

Autor: Jonatan Ortiz <jdortizc3@academia.usbbog.edu.co>
Fecha: 2025-05-22
"""

# Bibliotecas utilizadas:
# ------------------------
# - datetime: Para manejar fechas y horas (como la fecha de creación de tareas).
#             Documentación: https://docs.python.org/3/library/datetime.html
# - os: Para ejecutar comandos del sistema como limpiar la pantalla.
#       Documentación: https://docs.python.org/3/library/os.html

import datetime  
import os        

# Lista para guardar las tareas
tareas = []

def limpiar_pantalla():
    # Limpiar la pantalla (funciona en Windows y Unix)
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    print("========== MENÚ ==========")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Salir")

def agregar_tarea():
    nombre = input("Escribe la descripción de la tarea: ")
    fecha_creacion = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    tareas.append({"descripcion": nombre, "fecha": fecha_creacion, "completada": False})
    print("Tarea agregada correctamente.")

def ver_tareas():
    if len(tareas) == 0:
        print("No hay tareas registradas.")
    else:
        print("\nLista de tareas:")
        for i, tarea in enumerate(tareas):
            estado = "✔️" if tarea["completada"] else "❌"
            print(f"{i + 1}. [{estado}] {tarea['descripcion']} (Creada el {tarea['fecha']})")

def completar_tarea():
    ver_tareas()
    if len(tareas) == 0:
        return
    try:
        indice = int(input("Ingrese el número de la tarea a completar: ")) - 1
        if 0 <= indice < len(tareas):
            if not tareas[indice]["completada"]:
                tareas[indice]["completada"] = True
                print("Tarea marcada como completada.")
            else:
                print("La tarea ya estaba completada.")
        else:
            print("Número de tarea inválido.")
    except ValueError:
        print("Entrada inválida. Por favor ingrese un número.")

# Bucle principal
while True:
    limpiar_pantalla()
    mostrar_menu()
    opcion = input("Seleccione una opción (1-4): ")

    if opcion == '1':
        agregar_tarea()
    elif opcion == '2':
        ver_tareas()
    elif opcion == '3':
        completar_tarea()
    elif opcion == '4':
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intente de nuevo.")

    input("\nPresione Enter para continuar...")

# ========================
# LICENCIAS DE LAS LIBRERÍAS USADAS
# ========================

# 1. datetime (parte del módulo estándar de Python)
#    - Propósito: Manejo de fechas y horas.
#    - Licencia: Python Software Foundation License (PSFL)
#    - Más info: https://docs.python.org/3/library/datetime.html

# 2. os (parte del módulo estándar de Python)
#    - Propósito: Interacción con el sistema operativo.
#    - Licencia: Python Software Foundation License (PSFL)
#    - Más info: https://docs.python.org/3/library/os.html
