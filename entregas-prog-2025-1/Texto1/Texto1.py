def mostrar_menu():
    print("> Escriba 1 para pasar a minúsculas, ")
    print(">         2 para pasar a mayúsculas, ")
    print(">         3 para invertir mayúsculas y minúsculas ")
    print(">         4 para pasar a capitalización.")
    print(">         5 para pasar a titulación.")
    print(">         6 para reemplazar espacios por guiones bajos.")
    print(">         7 para mostrar texto original.")
    print(">         8 para salir.")
    print(">         9 para elegir otro texto.")

def main():
    # === PARTE LIBRE ===
    print("> Ingrese el texto que desea trabajar:")
    texto_usuario = input("< ")
    texto = (texto_usuario, texto_usuario)  # tupla: (original, modificado)

    # === MENÚ DE OPERACIONES ===
    while True:
        mostrar_menu()
        opcion = input("< ")
        modificado = texto[1]

        if opcion == '1':
            modificado = modificado.lower()
        elif opcion == '2':
            modificado = modificado.upper()
        elif opcion == '3':
            modificado = modificado.swapcase()
        elif opcion == '4':
            modificado = modificado.capitalize()
        elif opcion == '5':
            modificado = modificado.title()
        elif opcion == '6':
            modificado = modificado.replace(" ", "_")
        elif opcion == '7':
            print(f"> Texto original: {texto[0]}")
            continue
        elif opcion == '8':
            print("> Gracias!")
            break
        elif opcion == '9':
            print("> Ingrese el nuevo texto que desea trabajar:")
            nuevo_texto = input("< ")
            texto = (nuevo_texto, nuevo_texto)  # Reinicia original y modificado
            print("> Nuevo texto asignado correctamente.")
            continue
        else:
            print("> Opción no válida. Intente de nuevo.")
            continue

        texto = (texto[0], modificado)  # Actualiza solo el texto modificado
        print(f"> Resultado: {modificado}")

if __name__ == "__main__":
    main()