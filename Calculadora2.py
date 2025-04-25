"""
Título de práctica: Calculadora1

Calculadora con selección de operación

Autor: ElAutor <jdortizc3@academia.usbbog.edu.co>
Fecha: 2025-03-20
"""
print("Calculadora básica")

for _ in range(1000):  # Un rango grande para permitir múltiples operaciones
    # Convertimos las entradas a números

    operador = input("""
            Indique la operación a realizar:
         seleccione 1) Sumar
         seleccione 2) Restar
         seleccione 3) Multiplicar
         seleccione 4) Dividir
         seleccione 5) Potenciación
         seleccione 6) Módulo
         seleccione 7) Salir    
    """)
    num1 = float(input("Ingrese el primer operando: "))
    num2 = float(input("Ingrese el segundo operando: "))

    if operador == '1':
        resultado = num1 + num2
        print(f"El resultado de {num1} + {num2} es {resultado}")
    elif operador == '2':
        resultado = num1 - num2
        print(f"El resultado de {num1} - {num2} es {resultado}")
    elif operador == '3':
        resultado = num1 * num2
        print(f"El resultado de {num1} * {num2} es {resultado}")
    elif operador == '4':
        if num2 != 0:
            resultado = num1 / num2
            print(f"El resultado de {num1} / {num2} es {resultado}")
        else:
            print("Error: No se puede dividir entre cero.")
    elif operador == '5':
        resultado = num1 ** num2
        print(f"El resultado de {num1} elevado a {num2} es {resultado}")
    elif operador == '6':
        resultado = num1 % num2
        print(f"El módulo de {num1} % {num2} es {resultado}")
    elif operador == '7':
        print("Saliendo del programa.")
    else:
        print("Opción no válida.")
