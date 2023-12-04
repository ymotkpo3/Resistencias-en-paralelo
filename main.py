import sys
def obtener_resistencias():
    resistencias = []
    while True:
        valor = input("Ingrese un valor de resistencia (o 'N' para terminar): ")
        if valor.upper() == 'N':
            break
        try:
            resistencia = float(valor)
            resistencias.append(resistencia)
        except ValueError:
            print("Por favor, ingrese un número válido.")
    return resistencias
def calcular_resistencia_total(resistencias):
    if not resistencias:
        sys.exit("No se ingresaron resistencias. Terminando programa.")
    resistencias_inversas = [1 / r for r in resistencias]
    resistencia_total = 1 / sum(resistencias_inversas)
    return resistencia_total
def main():
    print("¡Bienvenido a la CALCULADORA DE RESISTENCIAS EN PARALELO!")
    if input("¿Desea comenzar? [S] [N]: ").upper() != "S":
        sys.exit("Se terminó la ejecución del programa.")
    resistencias = obtener_resistencias()
    resistencia_total = calcular_resistencia_total(resistencias)
    print(f"La resistencia total es de {resistencia_total:.2f} ohms")
if __name__ == "__main__":
    main()
