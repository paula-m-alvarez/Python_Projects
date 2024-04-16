import random


def adivina_el_numero(x):

    print("======================")
    print("Bievenid@ al Juego!")
    print("======================")
    print("Tu meta es adivinar el numero generado")

    numero_aleatorio = random.randint(1,x) # Generamos un numero entero aleatorio

    prediccionDelUsuario = 0 # Asi la primera vez no coincide con 1 y el usuario puede jugar

    while prediccionDelUsuario != numero_aleatorio:
        prediccionDelUsuario = int(input(f"Adivina un numero entre 1 y {x}: ")) # f-string / input siempre devuelve un stringnu

        if prediccionDelUsuario < numero_aleatorio:
            print("Intentra otra vez. Este numero es menor al que hay que adivinar")
        elif prediccionDelUsuario > numero_aleatorio:
            print("Intentra otra vez. Este numero es mayor al que hay que adivinar")

    print(f"Felicitaciones! Adivinaste el numero {numero_aleatorio} correctamente")


adivina_el_numero(10)