import json


class ManejadorJSON:
    def __init__(self):
        self.datos = []

    def importar(self, ruta):
        with open(ruta, "r", encoding="utf-8") as archivo:
            self.datos = json.load(archivo)
        return self.datos

    def modificar_valor(self, indice, clave, nuevo_valor):
        self.datos[indice][clave] = nuevo_valor

    def guardar(self, ruta):
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(self.datos, archivo, ensure_ascii=False, indent=2)