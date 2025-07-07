import json
import pickle
import os

"""
Práctica 1: Manejo de Archivos de Configuración
Esta práctica consiste en crear, leer y comparar archivos de configuración
en diferentes formatos: TXT, Pickle y JSON.
"""

def crear_config(id: int, datos: dict) -> None:
    """
    Crea tres archivos con la misma información de configuración:
    config{id}.txt, config{id}.pkl, config{id}.json
    """
    # Archivo TXT
    # Formato: Cada línea clave=valor, p.ej. usuario=jtorr
    txt_filename = f"config{id}.txt"
    with open(txt_filename, "w", encoding="utf-8") as f:
        f.write(f"usuario={datos['usuario']}\n")
        f.write(f"tema={datos['tema']}\n")
        f.write(f"volumen={datos['volumen']}\n")
        f.write(f"ventanas={','.join(datos['ventanas'])}\n") 
    print(f"Creado: {txt_filename}")

    # Archivo Pickle
    pkl_filename = f"config{id}.pkl"
    with open(pkl_filename, "wb") as f:
        pickle.dump(datos, f)
    print(f"Creado: {pkl_filename}")

    # Archivo JSON
    json_filename = f"config{id}.json"
    with open(json_filename, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=2, ensure_ascii=False)
    print(f"Creado: {json_filename}")

def leer_config_txt(id: int) -> dict:
    """
    Lee el contenido del archivo config{id}.txt y lo convierte en un diccionario.
    """
    txt_filename = f"config{id}.txt"
    config_data = {}
    if not os.path.exists(txt_filename):
        print(f"Error: El archivo {txt_filename} no existe.")
        return {}

    with open(txt_filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if "=" in line:
                key, value = line.split("=", 1)
                if key == "volumen":
                    config_data[key] = int(value)
                elif key == "ventanas":
                    config_data[key] = value.split(',')
                else:
                    config_data[key] = value
    return config_data

def leer_config_pickle(id: int) -> dict:
    """
    Lee el contenido del archivo config{id}.pkl y lo convierte en un diccionario.
    """
    pkl_filename = f"config{id}.pkl"
    if not os.path.exists(pkl_filename):
        print(f"Error: El archivo {pkl_filename} no existe.")
        return {}

    with open(pkl_filename, "rb") as f:
        config_data = pickle.load(f)
    return config_data

def leer_config_json(id: int) -> dict:
    """
    Lee el contenido del archivo config{id}.json y lo convierte en un diccionario.
    """
    json_filename = f"config{id}.json"
    if not os.path.exists(json_filename):
        print(f"Error: El archivo {json_filename} no existe.")
        return {}

    with open(json_filename, "r", encoding="utf-8") as f:
        config_data = json.load(f)
    return config_data

def imprimir_configuracion(id: int, config: dict):
    """
    Imprime la configuración de usuario en el formato especificado.
    """
    print(f"\nConfiguración {id}:")
    print(f"usuario: {config.get('usuario', 'N/A')}")
    print(f"tema: {config.get('tema', 'N/A')}")
    print(f"volumen: {config.get('volumen', 'N/A')}")
    print(f"ventanas: {config.get('ventanas', 'N/A')}")

def comparar_tamanios(id: int):
    """
    Muestra en consola el tamaño de los archivos TXT, Pickle y JSON.
    """
    txt_size = os.path.getsize(f"config{id}.txt")
    pkl_size = os.path.getsize(f"config{id}.pkl")
    json_size = os.path.getsize(f"config{id}.json")

    print(f"\nComparación de tamaños para config{id}:")
    print(f"Tamaño TXT: {txt_size} bytes")
    print(f"Tamaño Pickle: {pkl_size} bytes")
    print(f"Tamaño JSON: {json_size} bytes")


if __name__ == "__main__":
    # Datos de ejemplo para la configuración
    config_ejemplo_1 = {
        "usuario": "jtorr",
        "tema": "oscuro",
        "volumen": 75,
        "ventanas": ["principal", "secundaria"]
    }

    config_ejemplo_2 = {
        "usuario": "ana.m",
        "tema": "claro",
        "volumen": 90,
        "ventanas": ["ajustes", "notificaciones", "perfil"]
    }

    # ID de configuración
    config_id_1 = 1
    config_id_2 = 2

    print("--- Creando configuraciones ---")
    crear_config(config_id_1, config_ejemplo_1)
    crear_config(config_id_2, config_ejemplo_2)

    print("\n--- Leyendo configuraciones y mostrando por consola ---")

    # Leer y mostrar configuración TXT
    cfg_txt_1 = leer_config_txt(config_id_1)
    imprimir_configuracion(config_id_1, cfg_txt_1)

    cfg_txt_2 = leer_config_txt(config_id_2)
    imprimir_configuracion(config_id_2, cfg_txt_2)

    # Leer y mostrar configuración Pickle
    cfg_pkl_1 = leer_config_pickle(config_id_1)
    imprimir_configuracion(config_id_1, cfg_pkl_1)

    cfg_pkl_2 = leer_config_pickle(config_id_2)
    imprimir_configuracion(config_id_2, cfg_pkl_2)

    # Leer y mostrar configuración JSON
    cfg_json_1 = leer_config_json(config_id_1)
    imprimir_configuracion(config_id_1, cfg_json_1)

    cfg_json_2 = leer_config_json(config_id_2)
    imprimir_configuracion(config_id_2, cfg_json_2)

    print("\n--- Comparando tamaños de archivos ---")
    comparar_tamanios(config_id_1)
    comparar_tamanios(config_id_2)

    print("\nActividad completada. Los archivos han sido creados y leídos.")