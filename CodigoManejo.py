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
import seaborn as sns
import matplotlib.pyplot as plt

# Nos conectamos a la DB nuevamente
conn = sqlite3.connect('Covid/covid.sqlite')
cur = conn.cursor()

# Borro columna desde SQLite
# column_to_delete = 'Data_As_Of'
# cur.execute(f'ALTER TABLE covid DROP COLUMN {column_to_delete}')
# conn.commit()


df = pd.read_sql_query('SELECT * FROM covid', conn)
# df.info()

# Consulto por el Top 5 de estados con mas muertes por covid
consulta1 = '''
SELECT State, COVID_19_Deaths
FROM Covid
WHERE Age_Group = 'All Ages'
AND Sex = 'All Sexes'
AND Groups = 'By Total'
AND State != 'United States'
ORDER BY COVID_19_Deaths DESC
LIMIT 5
'''
datos = pd.read_sql_query(consulta1, conn)
# Crear el gráfico de barras utilizando Seaborn
sns.barplot(x='State', y='COVID_19_Deaths', data=datos)

plt.xlabel('Estados')
plt.ylabel('Número de Muertes por COVID-19')
plt.title('Muertes por COVID-19 por Estado')
# Roto etiquetas
plt.xticks(rotation=45)
plt.ylim(0, 130000)
# Muestro
plt.show()

consulta2 = '''
SELECT State, Pneumonia_Deaths
FROM Covid
WHERE Age_Group = 'All Ages'
AND Sex = 'All Sexes'
AND Groups = 'By Total'
AND State != 'United States'
ORDER BY Pneumonia_Deaths DESC
LIMIT 5
'''
datos2 = pd.read_sql_query(consulta2, conn)
sns.barplot(x='State', y='Pneumonia_Deaths', data=datos2)

plt.xlabel('Estados')
plt.ylabel('Número de Muertes por Neumonia')
plt.title('Muertes por Neumonia por Estado')
# Roto etiquetas
plt.xticks(rotation=45)
plt.ylim(0, 130000)
# Muestro
plt.show()

# Evalúo la correlacion entre las muertes de covid y neumonia en 5 estados 
variable1 = pd.read_sql_query(consulta1, conn)
variable2 = pd.read_sql_query(consulta2, conn)
conn.close()


datosCombinados = pd.merge(variable1, variable2, on='State')
# State es la variable que tienen en comun
Correlacion = datosCombinados['COVID_19_Deaths'].corr(datosCombinados['Pneumonia_Deaths'])
print('Correlacion de Muertes por Covid y Neumonia: ', Correlacion)


