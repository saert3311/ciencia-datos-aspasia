"""
La institución necesita su ayuda para crear un algoritmo que:
a) Reciba los dos últimos números de la placa y el número n de vehículos a
procesar.
b) Muestre la cantidad de placas de cada color de vehículo que es necesario
fabricar y reemplazar.
"""
from datetime import datetime
from faker import Faker

fake = Faker()

class ProcesadorPlacas:
    def __init__(self, lista_placas = []):
        self.__report = {
            'amarillas':0,
            'cafes':0,
            'rojas':0,
            'azules':0,
            'verdes':0,
        }
        self.__created_date = datetime.now()
        self.__plates = lista_placas

    
    def clasificar(self, plate):
        last = str(plate[-1]) #lo transformamos a STR por si llega en otro formato
        match last: #match es una maravilla que llego en 3.10 se puede hacer condiciones bastante complejas y es mucho mas eficiente
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

    def mostrarInformacion(self):
        for color, cantidad in self.__report.items():
            print(f'{color}: {cantidad}')

    def corridaClasificar(self):
        print('Clasificando Placas...')
        for color in self.__report.values():
            color = 0
        if len(self.__plates) > 0:
            for plate in self.__plates:
                self.clasificar(plate)
        print('Clasificacion Finalizada')
        self.mostrarInformacion()
        

def generarPlacas(cant: int, mostrar=False) -> list: #un metodo para generar una lista de patentes
    lista = []
    for _ in range(cant):
        lista.append(fake.ssn())
    if mostrar == True: print(lista)
    return lista



if __name__ == '__main__':
    lista1 = ProcesadorPlacas(generarPlacas(10, True))
    lista1.corridaClasificar()
    print('For the LoLs--->')
    lista2 = ProcesadorPlacas(generarPlacas(1000))
    lista2.corridaClasificar()