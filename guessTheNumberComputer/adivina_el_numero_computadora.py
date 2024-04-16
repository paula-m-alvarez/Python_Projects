import random


def adivina_el_numero_computadora(x):

    print("======================")
    print("Bievenid@ al Juego!")
    print("======================")
    print(f"Selecciona un numero entre 1 y {x} para que le computadora intente adivinarlo...")

    limite_minimo = 1
    limite_maximo = x

    respuesta = ""

    while respuesta != "c":
        if limite_minimo != limite_maximo:
            prediccion = random.randint(limite_minimo, limite_maximo)
        else:
            prediccion = limite_minimo

        respuesta = input(f"Mi preddcion es {prediccion}. Si es muy alta, ingresa (A). Si es muy baja, ingresa (B). Si es correcta, ingresa (C)").lower()

        if respuesta == "a":
            limite_maximo = prediccion - 1
        elif respuesta == "b":
            limite_minimo = prediccion + 1

    print(f"Sii la computadora adivino tu numero correctamente: {prediccion}")


adivina_el_numero_computadora(10)
        
