print("Calculadora básica")
print("Operaciones disponibles: suma (+), resta (-), multiplicación (*), división (/)")

num1 = float(input("Ingrese el primer número: "))
operador = input("Ingrese la operación (+, -, *, /): ")
num2 = float(input("Ingrese el segundo número: "))

if operador == '+':
    resultado = num1 + num2
    print(f"El resultado de {num1} + {num2} es {resultado}")
elif operador == '-':
    resultado = num1 - num2
    print(f"El resultado de {num1} - {num2} es {resultado}")
elif operador == '*':
    resultado = num1 * num2
    print(f"El resultado de {num1} * {num2} es {resultado}")
elif operador == '/':
        resultado = num1 / num2
        print(f"El resultado de {num1} / {num2} es {resultado}")
