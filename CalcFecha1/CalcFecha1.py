from datetime import datetime, timedelta

def calc_fecha():
    while True:
        fecha_actual = datetime.now()
        print(f"> La fecha actual es: {fecha_actual}")

        print("> Escriba 1 para ingresar segundos, ")
        print("         2 para ingresar dias,")
        print("         3 para salir.")
        opcion = input("< ")

        if opcion == '1':
            print("> Escriba la cantidad de segundos")
            try:
                segundos = int(input("< "))
                nueva_fecha = fecha_actual + timedelta(seconds=segundos)
                print(f"> La nueva fecha es: {nueva_fecha}")
            except ValueError:
                print("> Entrada inválida. Por favor ingrese un número entero.")
        
        elif opcion == '2':
            print("> Escriba la cantidad de días")
            try:
                dias = int(input("< "))
                nueva_fecha = fecha_actual + timedelta(days=dias)
                print(f"> La nueva fecha es: {nueva_fecha}")
            except ValueError:
                print("> Entrada inválida. Por favor ingrese un número entero.")
        
        elif opcion == '3':
            print("> Gracias!")
            break
        else:
            print("> Opción inválida. Intente de nuevo.")

# Ejecutar el programa
calc_fecha()
