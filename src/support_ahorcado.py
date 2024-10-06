import random
palabras = ["celebracion", "coche", "ciudad", "piñata", "emancipacion"]
palabra_secreta = random.choice(palabras)
palabra_oculta = ["_"] * len(palabra_secreta)
print("Palabra:", " ".join(palabra_oculta))

letras_adivinadas = []
intentos_fallidos = 0
max_intentos = 6  

while intentos_fallidos < max_intentos and "_" in palabra_oculta:
    print("Palabra: ", " ".join(palabra_oculta))
    letra = input("Dime una letra que creas que puede tenr la palabra: ").lower()

    if letra in letras_adivinadas:
        print("Ya has adivinado esa letra.")
    elif letra in palabra_secreta:
        for i in range(len(palabra_secreta)):
            if palabra_secreta[i] == letra:
                palabra_oculta[i] = letra
        letras_adivinadas.append(letra)
    else:
        intentos_fallidos += 1
        letras_adivinadas.append(letra)
        print(f"Letra incorrecta. Intentos fallidos: {intentos_fallidos}/{max_intentos}")

if "_" not in palabra_oculta:
    print(f"¡Felicidades! Adivinaste la palabra: {''.join(palabra_oculta)}")
else:
    print(f"Lo siento, has perdido. La palabra era: {palabra_secreta}")

