"""
    file: ejercicio6.py
    autor: davidpillco
"""
import csv

def lineasDiccionario(archivo):
    return csv.DictReader(archivo, delimiter =";")

with open("data/data-estudiantes.csv") as midata:
    
    datos = list(lineasDiccionario(midata))
    """
    # Se separa los nombres
    funcion = map(lambda x:list((x.items()))[0][1], datos)
    funcion2 =map(lambda x: x.split(" "), funcion)
    # Se extrae los nombres
    nombre = map(lambda x: x[1], funcion2)
    # Se separa los correos
    funcion3 = map(lambda x:list((x.items()))[1][1], datos)
    funcion4 = map(lambda x: x.split("."), funcion3)
    # Se extrae el correo sin la extencion
    correo = map(lambda x: x[0], funcion4)
    # Se imprime todo
    nombre_correo = (list(zip(nombre, correo)))
    print(list(map(lambda x: x[0]+"-"+x[1], nombre_correo)))
    """
    print(list(map(lambda x: "%s - %s"% (list(x.items())[0][1].split(" ")[1], list(x.items())[1][1].split(".")[0]), datos)))
    


