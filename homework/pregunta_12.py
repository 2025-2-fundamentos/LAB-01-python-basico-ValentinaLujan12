"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    with open("files/input/data.csv", "r") as file:
        data = file.readlines()

    resultado = {}

    for linea in data:
        columnas = linea.strip().split("\t")
        letra = columnas[0]
        col5 = columnas[4].split(",")  

        suma_valores = 0
        for par in col5:
            _, valor = par.split(":")
            suma_valores += int(valor)

        resultado[letra] = resultado.get(letra, 0) + suma_valores

    return dict(sorted(resultado.items()))
