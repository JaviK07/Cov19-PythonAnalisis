#Objetivo de script: De los 5 estados determinamos, según rango etario, que estado tuvo mas fallecidos por covid_19 en total segun sexo. -- Finalidad de analisis ver que estado sufrio mas decesos segun rango etarios
# Luego determinamos que género (del top 5) tuvo mas fallecidos, y lo muestro en grafico de barras -- Finalidad de este analisis: Determinar que genero es mas propenso a obitar

# Preparo los datos

# Muertes de Hombres
import sqlite3
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


conn = sqlite3.connect('Covid/covid.sqlite')
cur = conn.cursor()

consultaEstados = '''
SELECT DISTINCT *
FROM Covid
WHERE Groups = 'By Total'
AND Sex = 'Male'
AND Age_Group != 'All Ages'
AND State != 'United States'
AND (State = 'California' OR State = 'Texas' OR State = 'Florida' OR State = 'Pennsylvania' OR State = 'Ohio');
'''
Estados = cur.execute(consultaEstados)
DatosRevelados = Estados.fetchall()

# Creo nueva DB para almacenar datos de top5 estados con mas muertos por covid
ConnNuevaDB = sqlite3.connect('Covid/estados.sqlite')
cur1 = ConnNuevaDB.cursor()

cur1.execute(
    '''
    CREATE TABLE IF NOT EXISTS EstadosM (
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
        Footnote TEXT
    )
''')

insertar = '''
INSERT INTO EstadosM VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
'''
cur1.executemany(insertar, DatosRevelados)
ConnNuevaDB.commit()


# Muertes de Hombres
# Consultamos con un query segun rango etario y estado tuvo mas muertos (hombres):
ConsultaM = '''
    SELECT State, Age_Group, MAX(COVID_19_Deaths) AS Max_Deaths
    FROM EstadosM
    WHERE Age_Group
    GROUP BY Age_Group;
'''
QueryM = cur1.execute(ConsultaM)

datos_relevantesM = [fila for fila in QueryM]

# Determinamos que rango etario tuvo mas fallecidos en total (de los 5 estados)
print('TOP 1 DE ESTADOS CON MÁS CANTIDAD TOTAL DE HOMBRES FALLECIDOS SEGUN RANGO ETARIO POR COVID19','\n')
for fila in datos_relevantesM:
    estadoM, rangoEtarioM, fallecidosM = fila
    print('Estado:', estadoM, '--', 'Rango Etario:', rangoEtarioM, '--' ,'Cantidad Fallecidos:', fallecidosM, '\n')

# -----------------------------------------------------------------------------------------------------------------------------------------

# MUERTE DE MUJERES 
cur1.execute(
    '''
    CREATE TABLE IF NOT EXISTS EstadosF (
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
        Footnote TEXT
    )
''')

consultaEstados = '''
SELECT DISTINCT *
FROM Covid
WHERE Groups = 'By Total'
AND Sex = 'Female'
AND Age_Group != 'All Ages'
AND State != 'United States'
AND (State = 'California' OR State = 'Texas' OR State = 'Florida' OR State = 'Pennsylvania' OR State = 'Ohio');
'''
Estados = cur.execute(consultaEstados)
DatosRevelados = Estados.fetchall()

# Creo nueva DB para almacenar datos de top5 estados con mas muertos por covid
ConnNuevaDB = sqlite3.connect('Covid/estados.sqlite')
cur1 = ConnNuevaDB.cursor()

insertar = '''
INSERT INTO EstadosF VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
'''
cur1.executemany(insertar, DatosRevelados)
ConnNuevaDB.commit()

# -----------------------------------------------------------------------------------------------------------------------------------------


# Muertes de Hombres
# Consultamos con un query segun rango etario y estado tuvo mas muertos (hombres):
ConsultaF = '''
    SELECT State, Age_Group, MAX(COVID_19_Deaths) AS Max_Deaths
    FROM EstadosF
    WHERE Age_Group
    GROUP BY Age_Group;
'''
QueryF = cur1.execute(ConsultaF)
datos_relevantesF = [fila for fila in QueryF]


# Determinamos que rango etario y estado tuvo mas fallecidos en total (de los 5 estados)
print('\n')
print('TOP 1 DE ESTADOS CON MÁS CANTIDAD TOTAL DE MUJERES FALLECIDOS SEGUN RANGO ETARIO POR COVID19','\n')
for fila in datos_relevantesF:
    estadoF, rangoEtarioF, fallecidosF = fila
    print('Estado:', estadoF, '--', 'Rango Etario:', rangoEtarioF, '--' ,'Cantidad Fallecidos:', fallecidosF, '\n')

# -----------------------------------------------------------------------------------------------------------------------------------------


# Evaluo cantidad de muertes de mujeres en total comparado con hombres, haciendo grafico de barras
# Creo gráfico de columnas con Seaborn

# Hombres
consulta = '''
SELECT Age_Group, COVID_19_Deaths FROM EstadosM
'''
datos = pd.read_sql_query(consulta, ConnNuevaDB)

sns.barplot(x='Age_Group', y='COVID_19_Deaths', data=datos)

plt.xlabel('Rangos Etarios')
plt.ylabel('Fallecidos')
plt.title('Cantidad de Muertes por Rango Etario Masculino')
plt.show()

# -----------------------------------------------------------------------------------------------------------------------------------------

# Mujeres
consulta = '''
SELECT Age_Group, COVID_19_Deaths FROM EstadosF
'''
datos = pd.read_sql_query(consulta, ConnNuevaDB)

sns.barplot(x='Age_Group', y='COVID_19_Deaths', data=datos)


plt.xlabel('Rangos Etarios')
plt.ylabel('Fallecidos')
plt.title('Cantidad de Muertes por Rango Etario Femenino')

plt.show()

conn.close()
ConnNuevaDB.close()
# -----------------------------------------------------------------------------------------------------------------------------------------


















