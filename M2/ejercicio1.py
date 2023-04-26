"""
Manipular datos utilizando estructuras de vectores y matrices
acorde a la biblioteca Numpy para resolver problemas
"""

"""
Dadas 2 matrices con dimensiones similares, ¿cómo obtener una salida
de matriz en la que cada elemento es una suma de elementos de las 2
matrices? (solo puede usar numpy como librería, si realiza la matriz
con otro paquete el ejercicio no es válido)
"""
import numpy as np
from random import seed
from random import randint

seed()

def generator(min: int, max: int, size:int) -> list: #generamoos listas con elementos aleatorios
    random_values = []
    for i in range(size):
        random_values.append(randint(min, max))
    return random_values

array1 = np.array(generator(0,20,9)).reshape((3,3))
array2 = np.array(generator(0,20,9)).reshape((3,3))

print('Array 1: \n', array1)
print('Array 2: \n', array2)
print('Suma: \n', (array1 + array2))

# 2. Cree una matriz de identidad de dimensión 4.

identidad = np.identity(4)

print('Matriz Identidad: \n', identidad)

# 3. Convierte una matriz numpy binaria (que contiene solo 0 y 1) en una matriz numpy booleana.

matriz_bin = np.array(generator(0,1,10))
print('Matriz Binaria:\n',matriz_bin)
matriz_bin = matriz_bin.astype(bool)
print('Matriz Booleana:\n',matriz_bin)

# 4. Genere una secuencia de números en forma de matriz numpy de 0 a 100 con espacios de 2 números, por ejemplo: 0, 2, 4 ...

cero_cien = np.arange(0, 100, 2).reshape(10, 5)

print('Matriz generada:\n', cero_cien)