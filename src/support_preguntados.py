import random

catagerias = ["Geografía", "Historia", "Entretenimiento", "Ciencia"]

#GEOGRAFIA
preguntas_geografia = [{"Pregunta" : "¿Cuál es la capital de cantabria?","Respuestas" : {"Santander": True,"Lugo" : False,"Antequera" : False,"Oviedo" : False}},
 {"Pregunta" : "¿Cuál es la capital de Navarra?","Respuestas" : {"Alcalá de Henares": False,"Logroño" : False,"Pamplona" : True,"Zaragoza" : False}}]
preguntas_historia = [{"Pregunta" : "¿En que año se descubrió américa?","Respuestas" : {"1234": False,"1492" : True,"1482" : False,"1111" : False}},
 {"Pregunta" : "¿Quien fue el inventor del teléfono?","Respuestas" : {"Einsten": False,"Marie Curie" : False,"Alexander Graham Bell" : True,"Nicola Tesla" : False}}]
preguntas_entretenimiento = [{"Pregunta" : "¿Que famoso programador salío en Master Chef?","Respuestas" : {"James Gosling": False,"Jean-Charles" : True,"Guido Van Rossum" : False,"Dennis Ritchie" : False}},
 {"Pregunta" : "¿Que serie de estas las protagoniza el actor Huge Lauman?","Respuestas" : {"Ricky n' Morty": False,"Suits" : False,"La Que se Avecina" : False,"House" : True}}]
preguntas_ciencia = [{"Pregunta" : "¿Quien descubrió la penicilina?","Respuestas" : {"Alexander Fleming": True,"Da-Vinci" : False,"Isaac Newton" : False,"Blaise Pascal" : False}},
 {"Pregunta" : "¿Quien desarrollo el primer codigo de la historia?","Respuestas" : {"Ana Garcia Garcia": False,"Ada Lovelace" : True,"Steve Jobs" : False,"Ibai" : False}}]

eleccion = int(input(f"Elige una categoria sobre la que te quieras examinar: 1. Geografia 2. Historia 3. Entretenimiento 4. Ciencia"))


def ABCD(pregunta_aleatoria):
    print(pregunta_aleatoria["Pregunta"])

    respuestas = list(pregunta_aleatoria["Respuestas"].items())
    opciones = ['A', 'B', 'C', 'D']
    
    for i, (respuesta, _) in enumerate(respuestas):
        print(f"{opciones[i]}. {respuesta}")
    
    eleccion_usuario = input("Elige una opción (A, B, C, D): ").upper()

    if eleccion_usuario in opciones:
        indice_seleccionado = opciones.index(eleccion_usuario)
        respuesta_correcta = respuestas[indice_seleccionado][1]  

        if respuesta_correcta:
            print("¡Correcto!")
        else:
            print("MAAAAAL")

            
    else:
        print("Opción no válida. Elige entre A, B, C o D.")

if eleccion == 1:
    pregunta_aleatoria = random.choice(preguntas_geografia)
    ABCD(pregunta_aleatoria)
elif eleccion == 2:
    pregunta_aleatoria = random.choice(preguntas_historia)
    ABCD(pregunta_aleatoria)
elif eleccion == 3:
    pregunta_aleatoria = random.choice(preguntas_entretenimiento)
    ABCD(pregunta_aleatoria)
elif eleccion == 4:
    pregunta_aleatoria = random.choice(preguntas_ciencia)
    ABCD(pregunta_aleatoria)