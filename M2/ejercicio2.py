"""
Manipular datos utilizando estructuras de vectores y matrices
acorde a la biblioteca Numpy para resolver problemas
"""

"""
Escribir un programa que pregunte al usuario por las ventas de un rango
de años y muestre por pantalla una serie con los datos de las ventas
indexada por los años, antes y después de aplicarles un descuento del
10%.
"""
import pandas as pd
from faker import Faker
from random import uniform

fake = Faker()


def generar_calificaciones(cant: int) -> dict: #es menos latoso que introducir informacion
    data = {}
    for item in range(cant):
        data[fake.first_name()] = round(uniform(0, 10), 1)
    return data


def preguntar_usuario() -> dict:
    datos = {}
    while True:
        ano = input('Ingrese año de ventas:\n')
        valor = input('Ingrese valor de ventas:\n')
        datos[ano] = valor
        respuesta = (input('Desea agregar otro año S/N\n')).lower()
        if respuesta == 'n':
            break
    return datos


def procesar_datos(data) -> None:
    los_datos = pd.Series(preguntar_usuario(), dtype='int64', name='bruto') #ingesta de datos
    con_descuento = los_datos.apply(lambda x: x - (x*0.1)) # generamos una nueva serie calculando el descuento
    con_descuento = con_descuento.rename('descuento') # renombramos la serie para que se vea mejor cuando se imprima
    resumen = pd.concat([los_datos, con_descuento], axis=1) # concatenamos e imprimimos el dataframe resultante
    print('Resumen: \n', resumen)



"""
Escribir una función que reciba un diccionario con las notas de los
alumnos en curso en un examen y devuelva una serie con la nota
mínima, la máxima, media y la desviación típica.
"""

def analizar_notas(los_datos) -> pd.Series():
    serie = pd.Series(los_datos, dtype='float64')
    resumen = pd.Series({
        'minima': serie.min(),
        'maxima': serie.max(),
        'media': serie.median(),
        'desviacion': serie.std()
    })
    return resumen

"""
Escribir una función que reciba una diccionario con las notas de los
alumnos en curso en un examen y devuelva una serie con las notas de
los alumnos aprobados ordenadas de mayor a menor.
"""

def aprobados(datos: dict) -> pd.Series():
    calificaciones = pd.Series(datos, dtype='float64')
    print('Informacion sin filtrar (punto 3):\n',calificaciones)
    return calificaciones.sort_values(ascending=False)[calificaciones > 5]


DATOS = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril'],
    'Ventas': [30500, 35600, 28300, 33900],
    'Gastos': [22000, 23400, 18100, 20700]
}

def el_dataframe(datos: dict) -> pd.Series():
    dataframe = pd.DataFrame(datos)
    suma = dataframe.sum()
    dataframe = dataframe._append(suma, ignore_index=True)
    ultimo_indice = dataframe.iloc[-1].name
    dataframe.loc[ultimo_indice, 'Mes'] = 'Total'
    return dataframe


if __name__ == '__main__':
    #procesar_datos()
    print('Resumen calificaciones (punto2):\n',analizar_notas(generar_calificaciones(20)))
    print('Datos ordenados y filtrados:\n', aprobados(generar_calificaciones(10)))
    print('Informacion Dataframe (punto 4):\n', el_dataframe(DATOS))