#Objetivo de script: Separar en 5 bases de datos el top5 de estados
# Optimizar Script en otro script
import sqlite3

# Separo los 5 estados en 5 DB distintas

conn = sqlite3.connect('covid.sqlite')
cur = conn.cursor()

# Creación de conexiones para cada estado
conn1 = sqlite3.connect('california.sqlite')
conn2 = sqlite3.connect('texas.sqlite')
conn3 = sqlite3.connect('florida.sqlite')
conn4 = sqlite3.connect('pennsylvania.sqlite')
conn5 = sqlite3.connect('ohio.sqlite')

cur1 = conn1.cursor()
cur2 = conn2.cursor()
cur3 = conn3.cursor()
cur4 = conn4.cursor()
cur5 = conn5.cursor()

# Crear tablas para cada estado si aún no existen
cur1.execute('''
    CREATE TABLE IF NOT EXISTS California (
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

cur2.execute('''
    CREATE TABLE IF NOT EXISTS Texas (
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

cur3.execute('''
    CREATE TABLE IF NOT EXISTS Florida (
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

cur4.execute('''
    CREATE TABLE IF NOT EXISTS Pennsylvania (
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

cur5.execute('''
    CREATE TABLE IF NOT EXISTS Ohio (
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

# Consulta y copia de datos para California
consulta1 = '''
SELECT *
FROM Covid
WHERE State = 'California'
'''
cslt1 = cur.execute(consulta1)
datosAlmacenados1 = cslt1.fetchall()
insertar1 = '''
INSERT INTO California VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
'''
cur1.executemany(insertar1, datosAlmacenados1)

# Consulta y copia de datos para Texas
consulta2 = '''
SELECT *
FROM Covid
WHERE State = 'Texas'
'''
cslt2 = cur.execute(consulta2)
datosAlmacenados2 = cslt2.fetchall()
insertar2 = '''
INSERT INTO Texas VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
'''
cur2.executemany(insertar2, datosAlmacenados2)

# Consulta y copia de datos para Florida
consulta3 = '''
SELECT *
FROM Covid
WHERE State = 'Florida'
'''
cslt3 = cur.execute(consulta3)
datosAlmacenados3 = cslt3.fetchall()
insertar3 = '''
INSERT INTO Florida VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
'''
cur3.executemany(insertar3, datosAlmacenados3)

# Consulta y copia de datos para Pennsylvania
consulta4 = '''
SELECT *
FROM Covid
WHERE State = 'Pennsylvania'
'''
cslt4 = cur.execute(consulta4)
datosAlmacenados4 = cslt4.fetchall()
insertar4 = '''
INSERT INTO Pennsylvania VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
'''
cur4.executemany(insertar4, datosAlmacenados4)

# Consulta y copia de datos para Ohio
consulta5 = '''
SELECT *
FROM Covid
WHERE State = 'Ohio'
'''
cslt5 = cur.execute(consulta5)
datosAlmacenados5 = cslt5.fetchall()
insertar5 = '''
INSERT INTO Ohio VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
'''
cur5.executemany(insertar5, datosAlmacenados5)

# Commit y cierre de conexiones
conn1.commit()
conn2.commit()
conn3.commit()
conn4.commit()
conn5.commit()

cur.close()
cur1.close()
cur2.close()
cur3.close()
cur4.close()
cur5.close()







