"""
La institución necesita su ayuda para crear un algoritmo que:
a) Reciba los dos últimos números de la placa y el número n de vehículos a
procesar.
b) Muestre la cantidad de placas de cada color de vehículo que es necesario
fabricar y reemplazar.
"""
from datetime import datetime

class ProcesadorPlacas:
    def __init__(self, lista_placas = []):
        self.__report = {
            'amarillas':0,
            'cafes':0,
            'rojas':0,
            'azules:':0,
            'verdes':0,
        }
        self.__created_date = datetime.now()
        self.__plates = lista_placas

    
    def clasificar():
        for plate in self.__plates:
            match plate:
                case '1' | '2':
                    self.__report['amarillas'] += 1
                case '3' | '4':
                    self.__report['cafes'] += 1
                case '5' | '6':
                    self.__report['rojas'] += 1
                case '7' | '8':
                    self.__report['azules'] += 1
                case '9' | '0':
                    self.__report['verdes'] += 1


