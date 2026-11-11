import csv


class ManejadorCSV:
    def __init__(self):
        self.encabezados = []
        self.datos = []

    def importar(self, ruta):
        with open(ruta, "r", newline="", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            filas = list(lector)

        self.encabezados = filas[0]
        self.datos = filas[1:]
        return self.datos

    def modificar_valor(self, columna, indice, nuevo_valor):
        posicion = self.encabezados.index(columna)
        self.datos[indice][posicion] = str(nuevo_valor)

    def guardar(self, ruta):
        with open(ruta, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(self.encabezados)
            escritor.writerows(self.datos)