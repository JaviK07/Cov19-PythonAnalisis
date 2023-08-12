#Objetivo de script: De los 5 estados determinamos segun rango etaria que estado tuvo mas fallecidos por neumonia en total segun sexo (solamente la gráfica)

import sqlite3
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import exportCSV

conn1 = sqlite3.connect('Covid/covid.sqlite')
cur1 = conn1.cursor()

conn = sqlite3.connect('Covid/estados.sqlite')
cur = conn.cursor()


query1 = '''
SELECT State, COVID_19_Deaths
FROM Covid
WHERE Age_Group = 'All Ages'
AND Sex = 'All Sexes'
AND Groups = 'By Total'
AND State != 'United States'
ORDER BY Pneumonia_Deaths DESC
'''
query2 = '''
SELECT State, Pneumonia_Deaths
FROM Covid
WHERE Age_Group = 'All Ages'
AND Sex = 'All Sexes'
AND Groups = 'By Total'
AND State != 'United States'
ORDER BY Pneumonia_Deaths DESC
'''

# Evalúo la correlacion entre las muertes de covid y neumonia en 5 estados 
variable1 = pd.read_sql_query(query1, conn1)
variable2 = pd.read_sql_query(query2, conn1)
conn1.close()

datosCombinados = pd.merge(variable1, variable2, on='State')
# State es la variable que tienen en comun

# Hago calculo de correlacion entre muertes de neumonia y covid19 (a apartir de tabla covid.sqlite tomando la muestra completa para tener mayor confianza)
Correlacion = datosCombinados['COVID_19_Deaths'].corr(datosCombinados['Pneumonia_Deaths'])
print('Correlacion de Muertes por Covid y Neumonia: ', Correlacion)
# Correlacion de Muertes por Covid y Neumonia:  0.9870081706597609

# ------------------------------------------------------------------------------
# Grafico
consulta1 = '''
SELECT Age_Group, State, MAX(Pneumonia_Deaths) AS Max_Pneumonia_Deaths
FROM EstadosM
GROUP BY Age_Group;
'''

datos = pd.read_sql_query(consulta1, conn)

plt.figure(figsize=(10, 6))  # Ajusta el tamaño de la figura

sns.barplot(x='Age_Group', y='Max_Pneumonia_Deaths', data=datos)

# Añadir etiquetas de estado en cada barra
for index, row in datos.iterrows():
    plt.text(index, row['Max_Pneumonia_Deaths'], row['State'], color='black', ha="center")

plt.xlabel('Rangos Etarios')
plt.ylabel('Fallecidos')
plt.title('Estado con mayor cantidad de muertes de hombres por neumonía según rango etario')
plt.yticks(range(0, max(datos['Max_Pneumonia_Deaths']) + 1000, 1000))
plt.xticks(rotation=45)  # Rotar etiquetas del eje X para mayor legibilidad
plt.tight_layout()  # Ajustar el diseño
plt.show()

# ------------------------------------------------------------------------------
# Barras Mujeres

consulta2 = '''
SELECT Age_Group, State, MAX(Pneumonia_Deaths) AS Max_Pneumonia_Deaths
FROM EstadosF
GROUP BY Age_Group;
'''

datos = pd.read_sql_query(consulta2, conn)

plt.figure(figsize=(10, 6))  # Ajusta el tamaño de la figura

sns.barplot(x='Age_Group', y='Max_Pneumonia_Deaths', data=datos)

# Añadir etiquetas de estado en cada barra
for index, row in datos.iterrows():
    plt.text(index, row['Max_Pneumonia_Deaths'], row['State'], color='black', ha="center")

plt.xlabel('Rangos Etarios')
plt.ylabel('Fallecidos')
plt.title('Estado con mayor cantidad de muertes de mujeres por neumonía según rango etario')
plt.yticks(range(0, max(datos['Max_Pneumonia_Deaths']) + 1000, 1000))
plt.xticks(rotation=45)  # Rotar etiquetas del eje X para mayor legibilidad
plt.tight_layout()  # Ajustar el diseño
plt.show()

# Al calcular la correlación entre las muertes por COVID-19 y las muertes por neumonía (un valor cercano a 1), el resultado indica que ambas variables están estrechamente relacionadas. 
# Un valor cercano a 1 en la correlación sugiere que los fallecimientos por neumonía y los fallecimientos por COVID-19 tienden a aumentar o disminuir juntos, mostrando una fuerte relación lineal entre ellos.
# Representando visualmente los datos finales, podemos observar que tanto el género femenino como el masculino presentan cantidades similares de fallecimientos por ambas patologías. 
# Esto sugiere que la incidencia de muertes por COVID-19 y neumonía no muestra diferencias significativas entre los géneros. 
# Los hallazgos acerca de la cantidad de fallecidos de genero masculino y femenino indican que la población de género masculino podría tener una mayor probabilidad de fallecimiento, pero es importante tener en cuenta que para obtener una confirmación más precisa, 
# se necesitaría considerar otras variables relevantes de datos (tal como, condiciones de salud subyacentes, acceso a la atención médica, medidas de control y políticas públicas, capacidad del sistema de salud, entre otras.) 
# y realizar análisis complementarios.


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------///////
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------///////

# Exporto en CSV las DB para graficar en power BI
# exportCSV.Exportar_CSV()















