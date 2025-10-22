"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    with open("files/input/data.csv", "r") as archivo:
        datos = [linea.strip().split("\t")[:2] for linea in archivo]

    valores_por_letra = {}

    for letra, numero in datos:
        numero = int(numero)
        if letra not in valores_por_letra:
            valores_por_letra[letra] = [numero]
        else:
            valores_por_letra[letra].append(numero)

    resultado = []
    for letra in sorted(valores_por_letra.keys()):
        valores = valores_por_letra[letra]
        resultado.append((letra, max(valores), min(valores)))

    return resultado

