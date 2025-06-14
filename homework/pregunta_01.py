"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""
import pandas as pd
import os
import unicodedata

def pregunta_01():

    # Cargar el archivo CSV
    path_in = "files/input/solicitudes_de_credito.csv"
    path_out = "files/output/solicitudes_de_credito.csv"

    df = pd.read_csv(path_in, sep=";")

    df = df.dropna()

    # Limpieza columna 'sexo'
    df["sexo"] = df["sexo"].str.lower()

    # Limpieza columna 'tipo_de_emprendimiento'
    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.lower()

    # Limpieza columna 'idea_negocio'
    df["idea_negocio"] = df["idea_negocio"].str.lower().str.replace("_", " ").str.replace("-", " ").str.strip()

    # Limpieza columna 'barrio'
    df["barrio"] = df["barrio"].str.lower().str.replace("_", " ").str.replace("-", " ")

    # Limpieza columna 'fecha_de_beneficio'
    def normalizar_fecha(fecha):
        partes = fecha.split("/")
        if len(partes[0]) == 4:
            return f"{partes[2]}/{partes[1]}/{partes[0]}"
        return fecha

    df["fecha_de_beneficio"] = df["fecha_de_beneficio"].apply(normalizar_fecha)

    # Limpieza columna 'monto del credito'
    df["monto_del_credito"] = df["monto_del_credito"].str.replace(" ", "").str.replace("$", "").str.replace(",", "").astype(float)

    # Limpieza columna 'línea_credito'
    df["línea_credito"] = df["línea_credito"].str.lower().str.replace("_", " ").str.replace("-", " ")

    df = df.drop_duplicates(subset=[
        "sexo",
        "tipo_de_emprendimiento",
        "idea_negocio",
        "barrio",
        "estrato",
        "comuna_ciudadano",
        "fecha_de_beneficio",
        "monto_del_credito",
        "línea_credito",
    ])

    #Creamos carpeta de salida
    def output_directory(output_directory):
        if os.path.exists(output_directory):
            for file in glob.glob(f"{output_directory}/*"):
                os.remove(file)
            os.rmdir(output_directory)
        os.makedirs(output_directory)

    # Crear carpeta y guardar
    os.makedirs(os.path.dirname(path_out), exist_ok=True)
    df.to_csv(path_out, sep=";", index=False, encoding="utf-8")


    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """




pregunta_01()