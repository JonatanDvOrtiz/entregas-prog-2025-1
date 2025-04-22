print("Calculadora básica")

# Convertimos las entradas a números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
operador = input("> Escriba 1 para suma, 2 para resta, 3 para multiplicación, 4 para división, 5 para potenciación, 6 para módulo, 7 para salir: ")

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