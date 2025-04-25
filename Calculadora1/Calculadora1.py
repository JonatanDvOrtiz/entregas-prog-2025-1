
"""
Título de práctica: Calculadora1

Calculadora con selección de operación

Autor: JonatanOrtiz <jdortizc3@academia.usbbog.edu.co>
Fecha: 2025-03-13
"""
def run():
    # Ingreso de operandos
    num1 = float(input("Ingrese el primer operando: "))
    num2 = float(input("Ingrese el segundo operando: "))
    operador = input("""
            Indique la operación a realizar:
         seleccione 1) Sumar
         seleccione 2) Restar
         seleccione 3) Multiplicar
         seleccione 4) Dividir
          
    """)

    # Ejecuta operación indicada
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
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    run()