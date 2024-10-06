# main.py
import src.support_preguntados 
import src.support_piedrapapel 
import src.support_ahorcado

def mostrar_menu():
    print("\n===== Menú Principal =====")
    print("1. Jugar Piedra, Papel, Tijera, Lagarto, Spock")
    print("2. Jugar Preguntados")
    print("3. Jugar Ahorcado")
    print("4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            print("Has elegido jugar Piedra, Papel, Tijera, Lagarto, Spock")
            open(src.support_piedrapapel.py)
        elif opcion == "2":
            print("Has elegido jugar Preguntados")
            open(src.support_preguntados.py)
        elif opcion == "3":
            print("Has elegido jugar Ahorcado")
            open(src.support_ahorcado.py)
        elif opcion == "4":
            print("Saliendo del juego. ¡Hasta la próxima!")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")



