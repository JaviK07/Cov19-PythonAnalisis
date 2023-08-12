# El problema a resolver implica el análisis exhaustivo de datos relacionados con muertes por COVID-19 y neumonía, 
# recopilados entre el 1 de enero de 2020 y el 7 de enero de 2023. Estos datos están organizados en diferentes categorías, 
# como fecha de inicio y fin del registro, grupo de edad, sexo, estado o región, y otras variables relevantes. 
# Además de las muertes específicas por COVID-19 y neumonía, los registros también incluyen información sobre muertes por influenza y combinaciones de neumonía, influenza o COVID-19. 
# El objetivo de este análisis es identificar tendencias, patrones y correlaciones significativas en los datos, 
# con el fin de obtener una comprensión más profunda del impacto de estas enfermedades respiratorias en diferentes poblaciones y localidades. 
# La información extraída de este análisis puede ser crucial para informar futuras estrategias de salud pública, 
# tomar decisiones basadas en evidencia y mejorar la prevención y respuesta ante futuros brotes o pandemias.


import pandas as pd
import sqlite3


# Leemos primer relevamiento excel, según datos aportados los registros de 0-9 muertes no son registrados, por lo que procedemos a estandarizar a muertes =0
data = pd.read_csv('Covid/Relevamiento.csv')

data['COVID-19 Deaths'].fillna(0, inplace=True)
data['Total Deaths'].fillna(0, inplace=True)
data['Pneumonia and COVID-19 Deaths'].fillna(0, inplace=True)
data['Influenza Deaths'].fillna(0, inplace=True)
data['Pneumonia, Influenza, or COVID-19 Deaths'].fillna(0, inplace=True)
data['Footnote'].fillna('N/A', inplace=True)
data['Pneumonia Deaths'].fillna('0', inplace=True)

# Eliminamos columnas no requeridas
data.drop('Year', axis=1, inplace=True)
data.drop('Month', axis=1, inplace=True)



# Renombrar los nombres de las columnas
new_column_names = {
    'Data As Of': 'Data_As_Of',
    'Start Date': 'Start_Date',
    'End Date': 'End_Date',
    'Group': 'Groups',
    'Age Group': 'Age_Group',
    'COVID-19 Deaths': 'COVID_19_Deaths',
    'Pneumonia and COVID-19 Deaths': 'Pneumonia_and_COVID_19_Deaths',
    'Pneumonia Deaths' : 'Pneumonia_Deaths',
    'Influenza Deaths' : 'Influenza_Deaths',
    'Pneumonia, Influenza, or COVID-19 Deaths': 'Pneumonia_Influenza_or_COVID_19_Deaths',
    'Total Deaths' : 'Total_Deaths'
}
data.rename(columns=new_column_names, inplace=True)

# Se guarda el DataFrame completo con todas las columnas en un nuevo archivo CSV
ruta_guardado_csv = 'Covid/datamodificada.csv'
data.to_csv(ruta_guardado_csv, index=False)


# Pasamos a SQLite los datos
conn = sqlite3.connect('Covid/covid.sqlite')
cur = conn.cursor()

# Creamos tabla con columnas
cur.execute('''
        CREATE TABLE IF NOT EXISTS Covid (
        Data_As_Of TEXT NOT NULL,
        Start_Date TEXT NOT NULL,
        End_Date TEXT NOT NULL,
        Groups TEXT NOT NULL,
        State TEXT NOT NULL,
        Sex TEXT NOT NULL,
        Age_Group TEXT NOT NULL,
        COVID_19_Deaths INTEGER,
        Total_Deaths INTEGER,
        Pneumonia_Deaths INTEGER,
        Pneumonia_and_COVID_19_Deaths INTEGER,
        Influenza_Deaths INTEGER,
        Pneumonia_Influenza_or_COVID_19_Deaths INTEGER,
        Footnote TEXT ) 
            ''')
# Tomamos en nueva variable el set de datos
data1 = pd.read_csv('Covid/datamodificada.csv')
data1.to_sql('Covid', conn, if_exists='append', index=False)

conn.commit()
conn.close()

# Separamos los datos de tablas y generamos nuevas bases de datos con sqlite para luego exportar en CSV y pasarlo a power BI para hacer visuales














