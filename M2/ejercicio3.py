"""
1.- Crear un programa que sea capaz de leer el archivo videojuegos.csv,
luego sacar el promedio de los precios y el promedio de la calificación.
"""

import csv

def info_general(filename: str) -> None:
    precio_accum = 0
    calificacion_accum = 0
    with open(filename, newline='') as csvfile:
        reader =  csv.DictReader(csvfile)
        for line in reader:
            precio_accum += line['Precio']
            calificacion_accum += line['Calificacion']
        renglones = len(list(reader))
        promedio_precio = precio_accum / renglones
        promedio_calificacion = calificacion_accum / renglones
        print(f'El promedio de precio es: {promedio_precio}')
        print(f'El promedio de calificación es: {promedio_calificacion}')









if __name__ == '__main__':
    info_general('videojuegos.csv')