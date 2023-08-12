# Script de funcion para exportar a CSV con Pandas

import pandas as pd
import sqlite3

def Exportar_a_CSV_unaTabla():
    eleccion = input('Nombre de la DataBase: ')
    conexion = sqlite3.connect(eleccion)
    nombreTabla = input('nombre de tabla: ')
    query = f"SELECT * FROM {nombreTabla}"
    df = pd.read_sql_query(query, conexion)
    conexion.close()
    nombre_de_archivo = input('nombrá el archivo CSV: ')
    
    # Guardar registros en un archivo CSV
    df.to_csv(f"{nombre_de_archivo}.csv", index=False)
    print(f"Exportado exitosamente a {nombre_de_archivo}.csv")
# Exportar_a_CSV_unaTabla()


def Exportar_a_CSV_2tablas():
    eleccion = input('Nombre de la DataBase: ')
    conexion = sqlite3.connect(eleccion)

    # Consulta para obtener los datos de tabla1
    Tabla1 = input('Nombre de tabla1: ')
    query_tabla1 = f"SELECT * FROM {Tabla1}"
    df_tabla1 = pd.read_sql_query(query_tabla1, conexion)

    # Consulta para obtener los datos de tabla2
    Tabla2 = input('Nombre de tabla2: ')
    query_tabla2 = f"SELECT * FROM {Tabla2}"
    df_tabla2 = pd.read_sql_query(query_tabla2, conexion)
    conexion.close()

    # Concateno las tablas en un solo dataframe
    df_unido = pd.concat([df_tabla1, df_tabla2], ignore_index=True)

    nombre_de_archivo = input('nombrá el archivo CSV: ')
    
    # Guardar registros en un archivo CSV
    df_unido.to_csv(f"{nombre_de_archivo}.csv", index=False)
    print(f"Exportado exitosamente a {nombre_de_archivo}.csv")
# Exportar_a_CSV_2tablas()


def UnaTabla():
    Exportar_a_CSV_unaTabla()
def DosTablas():
    Exportar_a_CSV_2tablas()

def Exportar_CSV():

    print("\nMENU:")
    print("1. Una Tabla")
    print("2. Dos Tablas")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")
    if opcion == '1':
        UnaTabla()
    elif opcion == '2':
        DosTablas()
    elif opcion == '3':
        print("Saliendo del programa...")
    else:
        print("Opción inválida. Intente nuevamente.")




# README:
# Como importar a otro script:
# import exportCSV
# exportCSV.mostrar_menu()
