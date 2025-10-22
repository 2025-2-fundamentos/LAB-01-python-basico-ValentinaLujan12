"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    conteo = []
    with open("files/input/data.csv", "r") as file:
        entrada = [linea.split("\t")[0] for linea in list(file)]
        entrada.sort()
        letra_anterior = entrada[0]
        contador = 0
        for letra in entrada:
            if letra == letra_anterior:
                contador += 1
            else:
                conteo.append((letra_anterior, contador))
                contador = 1
            letra_anterior = letra
        conteo.append((letra_anterior, contador))

    return conteo