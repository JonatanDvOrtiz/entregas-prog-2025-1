from datetime import datetime, timedelta

def mostrar_fecha(fecha):
    return fecha.strftime('%d-%m-%Y %H:%M:%S')

def agregar_segundos(fecha_actual):
    print("> Escriba la cantidad de segundos")
    try:
        segundos = int(input("< "))
        nueva_fecha = fecha_actual + timedelta(seconds=segundos)
        print(f"> La nueva fecha es: {mostrar_fecha(nueva_fecha)}")
    except ValueError:
        print("> Entrada inválida. Por favor ingrese un número entero.")

def agregar_dias(fecha_actual):
    print("> Escriba la cantidad de días")
    try:
        dias = int(input("< "))
        nueva_fecha = fecha_actual + timedelta(days=dias)
        print(f"> La nueva fecha es: {mostrar_fecha(nueva_fecha)}")
    except ValueError:
        print("> Entrada inválida. Por favor ingrese un número entero.")

def run():
    print("Calculadora fecha")

def main():
    print("=== Calculadora de Fechas ===")
    print("Este programa le permite sumar segundos o días a la fecha actual.")

    while True:
        fecha_actual = datetime.now()
        print(f"> La fecha actual es: {mostrar_fecha(fecha_actual)}")

        print("> Escriba 1 para ingresar segundos, ")
        print("         2 para ingresar días,")
        print("         3 para salir.")
        opcion = input("< ")

        if opcion == '1':
            agregar_segundos(fecha_actual)
        elif opcion == '2':
            agregar_dias(fecha_actual)
        elif opcion == '3':
            print("> Gracias!")
            break
        else:
            print("> Opción inválida. Intente de nuevo.")

# Punto de entrada
if __name__ == "__main__":
    run()
    main()
