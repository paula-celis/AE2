class GeneradorResumenTXT:
    def generar(
        self,
        ruta,
        url_csv,
        url_json,
        archivo_csv,
        salida_csv,
        cambio_csv,
        cantidad_csv,
        archivo_json,
        salida_json,
        cambio_json,
        cantidad_json
    ):
        contenido = f"""RESUMEN DEL PROCESAMIENTO

URL de origen del CSV: {url_csv}
Archivo CSV importado: {archivo_csv}
Modificación realizada en CSV: {cambio_csv}
Nuevo CSV guardado: {salida_csv}
Registros CSV procesados: {cantidad_csv}

URL de origen del JSON: {url_json}
Archivo JSON importado: {archivo_json}
Modificación realizada en JSON: {cambio_json}
Nuevo JSON guardado: {salida_json}
Registros JSON procesados: {cantidad_json}

Clases y métodos utilizados:
- ManejadorCSV: importar, modificar_valor y guardar.
- ManejadorJSON: importar, modificar_valor y guardar.
- GeneradorResumenTXT: generar.
"""

        with open(ruta, "w", encoding="utf-8") as archivo:
            archivo.write(contenido)

        return ruta