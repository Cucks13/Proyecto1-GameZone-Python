# main.py

def mostrar_menu():
    print("\n===== Menú Principal =====")
    print("1. Jugar Piedra, Papel, Tijera, Lagarto, Spock")
    print("2. Jugar Preguntados")
    print("3. Jugar Tres en Raya")
    print("4. Jugar Ahorcado")
    print("5. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            print("\nHas elegido jugar Piedra, Papel, Tijera, Lagarto, Spock")
            ppt.iniciar_juego()  
        elif opcion == "2":
            print("\nHas elegido jugar Preguntados")
            preg.ABCD()  
        elif opcion == "3":
            print("\nHas elegido jugar Tres en Raya (aún no implementado)")
        elif opcion == "4":
            print("\nHas elegido jugar Ahorcado (aún no implementado)")
        elif opcion == "5":
            print("Saliendo del juego. ¡Hasta la próxima!")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


import src.support_preguntados as preg
import src.support_piedrapapel as ppt
