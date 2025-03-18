
"""
Título de práctica: Calculadora1

Calculadora con selección de operación

Autor: ElAutor <jdortizc3@academia.usbbog.edu.co>
Fecha: 2025-03-13
"""
numero1 = int(input("Introduzca el primer número"))
numero2 = int(input("Introduzca el segundo número"))

eleccion = 0
while eleccion !=6:
    print("""
            Indique la operación a relizar:
         seleccione 1)Sumar
         seleccione 2)Restar
         seleccione 3)Multiplicar
         seleccione 4)Dividir
          
    """)
    eleccion = int(input())
    if eleccion == 1:
        print(" ")
        print("Resultado: ",numero1,"+",numero2,"=",numero1+numero2)
    elif eleccion == 2:
        print(" ")
        print("Resultado: ",numero1,"-",numero2,"=",numero1-numero2)
    elif eleccion == 3:
        print(" ")
        print("Resultado: ",numero1,"x",numero2,"=",numero1*numero2)
    elif eleccion == 4:
        print(" ")
        print("Resultado: ",numero1,"/",numero2,"=",numero1/numero2)   
    elif eleccion == 5:
        print(" ")
        print("Resultado: ",numero1,"-",numero2,"=",numero1-numero2)    

