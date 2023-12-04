import sys

print("Hola, esta es LA CALCULADORA DE RESISTENCIAS EN PARALELO!! XD")

res = []

div1 = []

suma = 0.0

if input("desea comenzar? [S] [N]: ") == "S":
    pregunta = input(
        "desea ingresar un valor[numero] o no desea poner nada[N]?: ")

    if pregunta == "N":
        sys.exit("se termino la ejecucion del programa")
    else:
        res.append(float(pregunta))

    while pregunta != "N":
        repregunta = input(
            "desea ingresar otro valor[numero] o no desea poner nada mas[N]?: "
        )
        if repregunta == "N":
            break
        res.append(float(repregunta))

    if pregunta == "N":
        sys.exit("se termino la ejecucion del programa")

    print("dividiendo 1 por cada valor")

    for val in res:
        div1.append(1 / val)

    print("sumando valores")

    for value in div1:
        suma += value

    resultado = 1 / suma

    print("La resistencia total es de " + str(resultado) + " ohms")
