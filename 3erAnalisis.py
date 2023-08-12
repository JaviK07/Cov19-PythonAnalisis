# Muestro graficamente que cantidad de fallecidos totales hubieron por mes desde el inicio del dataset (neumonia y covid) - (todos los grupos de genero)
# Muestro en un solo grafico los muertos por covid (lineplot) segun estado

import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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

stateConsulta1 = '''
SELECT End_Date, State, COVID_19_Deaths, Pneumonia_Deaths
FROM newDBCovid
WHERE State = 'California';
'''
Datos1 = pd.read_sql_query(stateConsulta1, newDB)

Datos1['End_Date'] = pd.to_datetime(Datos1['End_Date'])
Datos1 = Datos1.sort_values(by='End_Date')

plt.figure(figsize=(12, 6))  # Tamaño del gráfico (opcional)
sns.lineplot(x='End_Date', y='COVID_19_Deaths', data=Datos1, label='COVID-19 Deaths')
sns.lineplot(x='End_Date', y='Pneumonia_Deaths', data=Datos1, linestyle = 'dashed', label='Pneumonia Deaths')


plt.xticks(rotation=45)
plt.xticks(Datos1['End_Date'].values, rotation=45, ha='right')

plt.title('Muertes por mes en California')
plt.xlabel('Meses')

plt.ylabel('Muertes')
plt.ylim(0, max(Datos1['COVID_19_Deaths']) * 1.1)

plt.legend()

# plt.show()

# -----------------------------------------------------------------------------

stateConsulta2 = '''
SELECT End_Date, State, COVID_19_Deaths, Pneumonia_Deaths
FROM newDBCovid
WHERE State = 'Texas';
'''
Datos2 = pd.read_sql_query(stateConsulta2, newDB)

Datos2['End_Date'] = pd.to_datetime(Datos2['End_Date'])
Datos2 = Datos2.sort_values(by='End_Date')

plt.figure(figsize=(12, 6))  # Tamaño del gráfico (opcional)
sns.lineplot(x='End_Date', y='COVID_19_Deaths', data=Datos2, label='COVID-19 Deaths')
sns.lineplot(x='End_Date', y='Pneumonia_Deaths', data=Datos2, linestyle = 'dashed', label='Pneumonia Deaths')


plt.xticks(rotation=45)
plt.xticks(Datos2['End_Date'].values, rotation=45, ha='right')

plt.title('Muertes por mes en Texas')
plt.xlabel('Meses')

plt.ylabel('Muertes')
plt.ylim(0, max(Datos2['COVID_19_Deaths']) * 1.1)

plt.legend()

# plt.show()

# -----------------------------------------------------------------------------

stateConsulta3 = '''
SELECT End_Date, State, COVID_19_Deaths, Pneumonia_Deaths 
FROM newDBCovid
WHERE State = 'Pennsylvania';
'''
Datos3 = pd.read_sql_query(stateConsulta3, newDB)

Datos3['End_Date'] = pd.to_datetime(Datos3['End_Date'])
Datos3 = Datos3.sort_values(by='End_Date')

plt.figure(figsize=(12, 6))  # Tamaño del gráfico (opcional)
sns.lineplot(x='End_Date', y='COVID_19_Deaths', data=Datos3, label='COVID-19 Deaths')
sns.lineplot(x='End_Date', y='Pneumonia_Deaths', data=Datos3, linestyle = 'dashed', label='Pneumonia Deaths')

plt.xticks(rotation=45)
plt.xticks(Datos3['End_Date'].values, rotation=45, ha='right')

plt.title('Muertes por mes en Pennsylvania')
plt.xlabel('Meses')

plt.ylabel('Muertes')
plt.ylim(0, max(Datos3['COVID_19_Deaths']) * 1.1)

plt.legend()

# plt.show()

# -----------------------------------------------------------------------------

stateConsulta4 = '''
SELECT End_Date, State, COVID_19_Deaths , Pneumonia_Deaths
FROM newDBCovid
WHERE State = 'Ohio';
'''
Datos4 = pd.read_sql_query(stateConsulta4, newDB)

Datos4['End_Date'] = pd.to_datetime(Datos4['End_Date'])
Datos4 = Datos4.sort_values(by='End_Date')

plt.figure(figsize=(12, 6))  # Tamaño del gráfico (opcional)
sns.lineplot(x='End_Date', y='COVID_19_Deaths', data=Datos4, label='COVID-19 Deaths')
sns.lineplot(x='End_Date', y='Pneumonia_Deaths', data=Datos4, linestyle = 'dashed', label='Pneumonia Deaths')

plt.xticks(rotation=45)
plt.xticks(Datos4['End_Date'].values, rotation=45, ha='right')

plt.title('Muertes por mes en Ohio')
plt.xlabel('Meses')

plt.ylabel('Muertes')
plt.ylim(0, max(Datos4['COVID_19_Deaths']) * 1.1)

plt.legend()

# plt.show()

# -----------------------------------------------------------------------------

stateConsulta5 = '''
SELECT End_Date, State, COVID_19_Deaths, Pneumonia_Deaths
FROM newDBCovid
WHERE State = 'Florida';
'''
Datos5 = pd.read_sql_query(stateConsulta5, newDB)

Datos5['End_Date'] = pd.to_datetime(Datos5['End_Date'])
Datos5 = Datos5.sort_values(by='End_Date')

plt.figure(figsize=(12, 6))  # Tamaño del gráfico (opcional)
sns.lineplot(x='End_Date', y='COVID_19_Deaths', data=Datos5, label='COVID-19 Deaths')
sns.lineplot(x='End_Date', y='Pneumonia_Deaths', data=Datos5, linestyle = 'dashed', label='Pneumonia Deaths')

plt.xticks(rotation=45)
plt.xticks(Datos5['End_Date'].values, rotation=45, ha='right')

plt.title('Muertes por mes en Florida')
plt.xlabel('Meses')

plt.ylabel('Muertes')
plt.ylim(0, max(Datos5['COVID_19_Deaths']) * 1.1)

plt.legend()

# plt.show()
# -----------------------------------------------------------------------------


# Crear el DataFrame con los datos de los estados que deseas graficar
estados = ['California', 'Texas', 'Pennsylvania', 'Ohio', 'Florida']
data_frames = []
for estado in estados:
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
plt.show()
newDB.close()


