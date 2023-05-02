"""
1.- Crear un programa que sea capaz de leer el archivo videojuegos.csv,
luego sacar el promedio de los precios y el promedio de la calificación.
"""

import csv

def info_general(filename: str) -> None:
    precio_accum = 0
    calificacion_accum = 0
    renglones = 0
    with open(filename, newline='') as csvfile:
        reader =  csv.DictReader(csvfile, delimiter=';')
        for line in reader:
            precio_accum += float(line['Precio'])
            calificacion_accum += int(line['Calificacion'])
            renglones += 1
        promedio_precio = precio_accum / renglones
        promedio_calificacion = calificacion_accum / renglones
        print(f'El promedio de precio es: {round(promedio_precio, 2)}')
        print(f'El promedio de calificación es: {round(promedio_calificacion, 2)}')

"""
a) La función juegosConsolas(nomArchivo, categoria, decada) que recibe el
nombre del archivo con la información de los videojuegos, una categoría y
número de cuatro dígitos representando una década de años. La función
retorna una tupla con 2 elementos. El primer elemento es la lista con los
valores únicos de todos los juegos de esa década para esa categoría. El
segundo elemento es la lista con valores únicos de todas las consolas que
tienen juegos para esa década y categoría.
Por ejemplo, para llamar
a juegosConsolas('videojuegos.csv','RPG',1980) retorna:

(['The legend of Zelda', 'Phantasy Star', ...], ['NES', 'Famicon Disk System', ...])
"""


def juegosConsolas(filename: str, categoria: str, buscar_decada: str) -> tuple:
    def get_decada(ano):
        dividido = list(str(ano).replace("'", ""))
        return dividido[-2]
    juegos = []
    consolas = []
    with open(filename) as File:
        reader = csv.reader(File, delimiter=';', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        for idx, line in enumerate(reader):
            if idx == 0: continue #no me interesan los indices
            divididos = str(line[0]).split(',')
            if get_decada(buscar_decada) == get_decada(divididos[1]):
                if categoria.lower() == divididos[-1].lower():
                    juegos.append(divididos[0])
                    consolas.extend(divididos[2:-2])
    return (list(set(juegos)), list(set(consolas)))

            
"""
b) La función crearMatriz(nomArchivo, categoria, decada) que recibe el
nombre del archivo con la información de los videojuegos, el nombre de una
categoría de videojuegos y un número de cuatro dígitos representando una
década de años. La función deberá leer el archivo y retorna una matriz donde
las filas representan los juegos de categoría para la década , las columnas
representan las consolas que tienen juegos de categoría para la década y las
celdas son las calificaciones de cada juego para cada consola. Si un juego no
existe para una consola, su calificación deberá ser cero (0).
"""

def crearMatriz(filename: str, categoria: str, buscar_decada: str) -> list:
    def get_decada(ano):
        dividido = list(str(ano).replace("'", ""))
        return dividido[-2]
    cabecera = ['juego',]
    consolas = []
    datos_limpios = []
    matriz = []

    with open(filename) as File:
        reader = csv.reader(File, delimiter=';', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        for idx, line in enumerate(reader):
            if idx == 0: continue #no me interesan los indices
            divididos = str(line[0]).split(',')
            if get_decada(buscar_decada) == get_decada(divididos[1]) and categoria.lower() == divididos[-1].lower():
                datos_limpios.append(divididos)
                consolas.extend(divididos[2:-2])
    consolas = list(set(consolas))
    cabecera.extend(consolas)
    matriz.append(cabecera)
    for file in range(len(datos_limpios)):
        row = [datos_limpios[file][0]]
        row.extend([0] * (len(cabecera) - 1))
        matriz.append(row)

    matriz_unica = []
    for lst in matriz:
        if lst not in matriz_unica:
            matriz_unica.append(lst)

    def ubicar_en_matriz(nombre: str, calificacion: str, consola:str) -> None:
            for row in range(1, len(matriz_unica)):
                if nombre in matriz_unica[row]:
                    index = matriz_unica[0].index(consola)
                    matriz_unica[row][index] = calificacion


    for i in datos_limpios:
        consolas = i[2:-2]
        for consola in consolas:
            ubicar_en_matriz(i[0], i[-2], consola)

    for line in matriz_unica:
        print(line)



if __name__ == '__main__':
    info_general('videojuegos.csv')
    print('Requerimiento a:\n',juegosConsolas('videojuegos2.csv','RPG',1980))
    print('Requerimiento b')
    crearMatriz('videojuegos2.csv','RPG',1980)