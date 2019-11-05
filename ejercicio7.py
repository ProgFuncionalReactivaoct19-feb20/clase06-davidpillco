"""
    file: ejercicio7.py
    autor: davidpillco
"""
import csv
# Lectura del archivo
def lineasDiccionario(archivo):
    return csv.DictReader(archivo, delimiter ="\t")

with open("data/trabajadores.csv") as midata:
    datos = list(lineasDiccionario(midata))
# Evaluacion del registro
    funcion = filter(lambda x: len(list(x.items())[2][1]) >= 10, datos)
# Print final
    print(list(sorted(funcion, key =lambda x: list(x.items())[1][1].split("-")[2])))