"""
    file: ejercicio3.py
    autor: davidpillco
"""
import csv
def lineas(archivo):
    return csv.reader(archivo, delimiter= ";")

with open("data/data-estudiantes.csv") as midata:
    print(list(lineas(midata)))


# midata = open("data/data-estudiantes.csv") # en usos de grandes volumenes de ?\
    # datos es necesario cerra el archivo *.
# print (list(lienas(midata)))
# midata.close()
