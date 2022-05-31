# -*- coding: utf-8 -*-
"""
Created on Thu May 26 10:35:59 2022

@author: smenco
"""
import pandas as pd
import matplotlib.pyplot as plt

url = 'Casos_positivos_de_COVID-19_en_Colombia.csv'
data = pd.read_csv(url) 

data.drop('Código ISO del país', axis = 1, inplace=True)
data.drop('Nombre del país', axis = 1, inplace=True)
data.drop('Pertenencia étnica', axis = 1, inplace=True)
data.drop('Nombre del grupo étnico', axis = 1, inplace=True)
data.drop('Fecha de inicio de síntomas', axis = 1, inplace=True)
data.drop('Unidad de medida de edad', axis = 1, inplace=True)
data.drop('Código DIVIPOLA departamento', axis = 1, inplace=True)
data.drop('Código DIVIPOLA municipio', axis = 1, inplace=True)
data.drop('ID de caso', axis = 1, inplace=True)

aux = data['Recuperado'].value_counts()

data.loc[data['Estado'] == 'leve'] = 'Leve'
data.loc[data['Estado'] == 'LEVE'] = 'Leve'

data.loc[data['Ubicación del caso'] == 'casa'] = 'Casa'
data.loc[data['Ubicación del caso'] == 'CASA'] = 'Casa'

data.loc[data['Sexo'] == 'm'] = 'M'
data.loc[data['Sexo'] == 'f'] = 'F'

data.loc[data['Edad'] == 'Casa'] = 36
data.loc[data['Edad'] == 'Leve'] = 36
data.loc[data['Edad'] == 'M'] = 36
data.loc[data['Edad'] == 'F'] = 36


data.mean()

#Número de casos de Contagiados en el País.
data['Estado'].count()

#Número de Municipios Afectados
data['Nombre municipio'].nunique()

#Liste los municipios afectados (sin repetirlos)
data['Nombre municipio'].value_counts()

#Número de personas que se encuentran en atención en casa
aux = data.loc[(data['Ubicación del caso'] == 'Casa')]
NumeroDePersonasEnCasa = aux.shape[0]

#Número de personas que se encuentran recuperados
aux = data.loc[(data['Recuperado'] == 'Recuperado')]
NumeroDePersonasRecuper = aux.shape[0]

#Número de personas que ha fallecido
aux = data.loc[(data['Estado'] == 'Fallecido')]
NumeroDePersonasFallecidas = aux.shape[0]

#Ordenar de Mayor a menor por tipo de caso (Importado, en estudio,Relacionado)
data.sort_values(by=data.loc[(data['Tipo de contagio'] == 'Importado')],ascending=False )
data.sort_values(by=data.loc[(data['Tipo de contagio'] == 'Relacionado')],ascending=False )
#Número de departamentos afectados
data['Nombre departamento'].nunique()

#Liste los departamentos afectados(sin repetirlos)
data['Nombre departamento'].value_counts()

data[data['Edad'] == '']


#Ordene de mayor a menor por tipo de atención
data.sort_values(by='Tipo de recuperación',ascending=False )

#Liste de mayor a menor los 10 departamentos con mas casos de contagiados
data['Nombre departamento'].value_counts().head(10)

#Liste de mayor a menor los 10 departamentos con mas casos de fallecidos
aux = data[(data['Estado'] == 'Fallecido')].groupby('Nombre departamento').size()

aux.sort_values(ascending=False).head(10)

#Liste de mayor a menor los 10 departamentos con mas casos de recuperados
aux = data[(data['Recuperado'] == 'Recuperado')].groupby('Nombre departamento').size()

aux.sort_values(ascending=False).head(10)

#Liste de mayor a menor los 10 municipios con mas casos de contagiados
data['Nombre municipio'].value_counts().head(10)

#Liste de mayor a menor los 10 municipios con mas casos de fallecidos
aux = data[(data['Estado'] == 'Fallecido')].groupby('Nombre municipio').size()

aux.sort_values(ascending=False).head(10)

#Liste de mayor a menor los 10 municipios con mas casos de recuperados
aux = data[(data['Recuperado'] == 'Recuperado')].groupby('Nombre municipio').size()

aux.sort_values(ascending=False).head(10)

#Liste agrupado por departamento y en orden de Mayor a menor las ciudades con mas casos de contagiados
aux = data.groupby(['Nombre departamento', 'Nombre municipio']).size()

aux.sort_values(ascending=False)

#Número de Mujeres y hombres contagiados por ciudad por departamento
aux = data.groupby(['Nombre departamento', 'Nombre municipio', 'Sexo']).size()

aux.sort_values(ascending=False)

#Liste el promedio de edad de contagiados por hombre y mujeres por ciudad por departamento
data.groupby(['Nombre departamento', 'Nombre municipio', 'Sexo'])['Edad'].mean()

#Liste de mayor a menor el número de contagiados por país de procedencia
aux = data.groupby(['Nombre del país']).size()

aux.sort_values(ascending=False)

#Liste de mayor a menor las fechas donde se presentaron mas contagios
aux = data.groupby(['Fecha de diagnóstico']).size()

aux.sort_values(ascending=False)

#Diga cual es la tasa de mortalidad y recuperación que tiene toda Colombia

cantidad_muertes = data[data['Estado'] == 'Fallecido'].shape[0]
cantidad_recuperados = data.query('Recuperado == "Recuperado"').shape[0]
cantidad_casos = data.shape[0]

tasa_mortalidad = cantidad_muertes / cantidad_casos * 100

tasa_recuperacion = cantidad_recuperados / cantidad_casos * 100

#Liste la tasa de mortalidad y recuperación que tiene cada departamento

cantidad_muertes_dep = data[data['Estado'] == 'Fallecido'].groupby('Nombre departamento').size()
cantidad_recuperados_dep = data[data['Recuperado'] == 'Recuperado'].groupby('Nombre departamento').size()
cantidad_casos_dep = data.groupby('Nombre departamento').size()

tasa_mortalidad_dep = cantidad_muertes_dep / cantidad_casos_dep * 100

tasa_recuperacion_dep = cantidad_recuperados_dep / cantidad_casos_dep * 100

data2 = pd.DataFrame({'tasa_mortalidad_dep': tasa_mortalidad_dep, 'tasa_recuperacion_dep':tasa_recuperacion_dep})

#Liste la tasa de mortalidad y recuperación que tiene cada ciudad

cantidad_muertes_ciu = data[data['Estado'] == 'Fallecido'].groupby('Nombre municipio').size()
cantidad_recuperados_ciu = data[data['Recuperado'] == 'Recuperado'].groupby('Nombre municipio').size()
cantidad_casos_ciu = data.groupby('Nombre municipio').size()

tasa_mortalidad_ciu = cantidad_muertes_ciu / cantidad_casos_ciu * 100

tasa_recuperacion_ciu = cantidad_recuperados_ciu / cantidad_casos_ciu * 100

data3 = pd.DataFrame({'tasa_mortalidad_ciu': tasa_mortalidad_ciu, 'tasa_recuperacion_ciu':tasa_recuperacion_ciu})

#Liste por cada ciudad la cantidad de personas por atención

data.groupby(['Nombre municipio', 'Tipo de recuperación']).size()

#Liste el promedio de edad por sexo por cada ciudad de contagiados

data.groupby(['Nombre municipio', 'Sexo'])['Edad'].mean()