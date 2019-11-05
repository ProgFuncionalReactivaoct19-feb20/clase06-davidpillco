"""
    file: ejercicio4.py
    autor: davidpillco
"""
import csv
def lineas(archivo):
    return csv.reader(archivo, delimiter= ";")
with open("data/data-estudiantes.csv") as midata:
    datos = list(lineas(midata))
    print(list(map(lambda x: x[1], filter(lambda x: x[1] != "email",datos))))
