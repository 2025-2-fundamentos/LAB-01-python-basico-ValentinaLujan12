"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    conteo_por_letra = []

    with open("files/input/data.csv", "r") as archivo:
        datos = [linea.strip().split("\t")[:2] for linea in archivo]

    datos.sort(key=lambda x: x[0])

    letra_actual = None
    acumulado = 0

    for letra, valor in datos:
        valor = int(valor)
        if letra != letra_actual:
            if letra_actual is not None:
                conteo_por_letra.append((letra_actual, acumulado))
            letra_actual = letra
            acumulado = valor
        else:
            acumulado += valor

    if letra_actual is not None:
        conteo_por_letra.append((letra_actual, acumulado))

    return conteo_por_letra
