# Muestro graficamente que cantidad de fallecidos totales hubieron por mes desde el inicio del dataset (neumonia y covid) - (todos los grupos de genero)
# Muestro en un solo grafico los muertos por covid (lineplot) segun estado

import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import exportCSV

# Genero nueva DB unicamente con datos relevados por mes (unicamente top5)
conn = sqlite3.connect('Covid/covid.sqlite')
cur = conn.cursor()

newDB = sqlite3.connect('Covid/newCovidDB.sqlite')
curNewDB = newDB.cursor()

curNewDB.execute('''
        CREATE TABLE IF NOT EXISTS newDBCovid (
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

query = '''
SELECT *
FROM Covid
WHERE Groups = 'By Month'
AND Sex = 'All Sexes'
AND Age_Group = 'All Ages'
AND (State = 'California' OR State = 'Texas' OR State = 'Pennsylvania' OR State = 'Florida' OR State = 'Ohio');
'''

datos = cur.execute(query)
revelado = datos.fetchall()
curNewDB.executemany('''INSERT INTO newDBCovid VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', revelado)

newDB.commit()
conn.close()


# -----------------------------------------------------------------------------
Estados = ['California', 'Texas', 'Florida', 'Pennsylvania', 'Ohio']

for estado in Estados:
    stateConsulta = f'''
    SELECT End_Date, State, COVID_19_Deaths, Pneumonia_Deaths
    FROM newDBCovid
    WHERE State = '{estado}' ;
    '''
    datos = pd.read_sql_query(stateConsulta, newDB)
    datos['End_Date'] = pd.to_datetime(datos['End_Date'])
    datos = datos.sort_values(by='End_Date')
    # print(datos)
    plt.figure(figsize=(12,6))
    sns.lineplot(x='End_Date', y='COVID_19_Deaths', data=datos, label='COVID-19 Deaths')
    sns.lineplot(x= 'End_Date', y='Pneumonia_Deaths', data=datos, linestyle='dashed', label='Pneumonia Deaths')
    plt.xticks(rotation =45)
    plt.xticks(datos['End_Date'].values, rotation=45, ha='right')
    plt.title(f'Muertes por mes en {estado}')
    plt.xlabel('Meses')
    plt.ylabel('Muertes')
    plt.ylim(0, max(datos['COVID_19_Deaths'])*1.1)
    plt.legend()
    # Mostrar ↓
    plt.show()

# # -----------------------------------------------------------------------------


# Creo el DataFrame con los datos de los estados a graficar
data_frames = []
for estado in Estados:
    stateConsulta = f'''
        SELECT End_Date, State, COVID_19_Deaths 
        FROM newDBCovid
        WHERE State = '{estado}';
    '''
    datos_estado = pd.read_sql_query(stateConsulta, newDB)
    datos_estado['End_Date'] = pd.to_datetime(datos_estado['End_Date'])
    data_frames.append(datos_estado)
    # print(data_frames)

# Concateno los dataframes de cada estado en uno solo
datos_totales = pd.concat(data_frames)

# Crear el gráfico de líneas con múltiples líneas diferenciadas por el estado
plt.figure(figsize=(12, 8))  
sns.lineplot(x='End_Date', y='COVID_19_Deaths', hue='State', data=datos_totales)

plt.xticks(rotation=45)
plt.title('Muertes por mes en diferentes estados')
plt.xlabel('Meses')
plt.ylabel('Muertes')

plt.legend(title='Estado')
# Mostrar ↓
# plt.show()
newDB.close()


# exportCSV.Exportar_CSV()