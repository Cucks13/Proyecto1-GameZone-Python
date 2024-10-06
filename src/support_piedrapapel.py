import random
import time

lista_opciones = ["PIEDRA", "PAPEL", "TIJERA", "LAGARTO", "SPOCK"]

def jugar(jugador, maquina):
    if jugador == maquina:
        return "Empate"
    elif (jugador == "PIEDRA" and (maquina == "TIJERA" or maquina == "LAGARTO")):
        return "Me ganaste"
    elif (jugador == "PAPEL" and (maquina == "PIEDRA" or maquina == "SPOCK")):
        return "Me ganaste"
    elif (jugador == "TIJERA" and (maquina == "PAPEL" or maquina == "LAGARTO")):
        return "Me ganaste"
    elif (jugador == "LAGARTO" and (maquina == "SPOCK" or maquina == "PAPEL")):
        return "Me ganaste"
    elif (jugador == "SPOCK" and (maquina == "TIJERA" or maquina == "PIEDRA")):
        return "Me ganaste"
    else:    
        return "Te gané"
    
def obtener_opcion_jugador():
    jugador = input(f"Escribe la opción que quieras para competir {lista_opciones}: ").upper()
    while jugador not in lista_opciones:
        print("Opción inválida. Inténtalo de nuevo.")
        jugador = input(f"Escribe la opción que quieras para competir {lista_opciones}: ").upper()
    return jugador

def iniciar_juego():
    contador_jugador = 0
    contador_maquina = 0

    while contador_jugador < 3 and contador_maquina < 3:
        # Obtener elección del jugador y la máquina
        jugador = obtener_opcion_jugador()
        maquina = random.choice(lista_opciones)

        # Jugar una ronda
        resultado = jugar(jugador, maquina)
        if resultado == "Me ganaste":
            contador_jugador += 1
            print(f"Me ganaste Jugador: {jugador}, Máquina: {maquina}")
        elif resultado == "Te gané":
            contador_maquina += 1
            print(f"Te gané Jugador: {jugador}, Máquina: {maquina}")
        else:
            print(f"otra, otra Jugador: {jugador}, Máquina: {maquina}")
        
        # Mostrar el marcador
        print(f"Marcador - Jugador: {contador_jugador}, Máquina: {contador_maquina}")
        
        # Pausa de 1 segundo antes de la siguiente ronda
        time.sleep(1)

    # Declarar el ganador
    if contador_jugador == 3:
        print("GANASTE, EL REY DEL LUGAR")
    else:
        print("PERDEDOR, QUIERES REVANCHA¿?¿?")

while True:
    iniciar_juego()
    # Preguntar si el jugador quiere volver a jugar
    jugar_otra_vez = input("¿REVANCHA? (si/no): ").lower()
    if jugar_otra_vez != "si":
        print("CAGAO")
        break
