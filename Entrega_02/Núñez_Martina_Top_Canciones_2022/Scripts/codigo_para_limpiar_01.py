# -*- coding: utf-8 -*-
"""Entrega 02 - NGN

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bzxc3DGG9p-QZG7Jn7PhmFVPeRki7WtR

Limpiamos las base de datos de Chile, Colombia, Argentina, Perú, Guatemala, Honduras, México y España, junto con el top global. Todos correspondiente al año 2022.
"""

import pandas as pd

#Importamos el archivo "Chile_2022" desde nuestro Drive
Chile_2022 = pd.read_csv('/content/drive/MyDrive/BASES DE DATOS/Chile_2022.csv')

#Vemos las columnas que tiene nuestro csv
print(Chile_2022.columns)

#Limpiamos la base de datos y quitamos las columnas que no son necesarias para la investigación del proyecto
Chile_2022_limpio = Chile_2022.drop(['uri', 'source', 'previous_rank'], axis=1)

#Guardamos nuestra base de datos limpia en nuestro Drive
Chile_2022_limpio.to_csv('/content/drive/MyDrive/BASES DE DATOS/Chile_2022_limpio.csv', index=False)  # Agregamos "index=False" para evitar que se guarde el índice en el archivo CSV.

import pandas as pd

#Importamos el archivo "Colombia_2022" desde nuestro Drive
Colombia_2022 = pd.read_csv('/content/drive/MyDrive/BASES DE DATOS/Colombia_2022.csv')

#Vemos las columnas que tiene nuestro csv
print(Colombia_2022.columns)

#Limpiamos la base de datos y quitamos las columnas que no son necesarias para la investigación del proyecto
Colombia_2022_limpio = Colombia_2022.drop(['uri', 'source', 'previous_rank'], axis=1)

#Guardamos nuestra base de datos limpia en nuestro Drive
Colombia_2022_limpio.to_csv('/content/drive/MyDrive/BASES DE DATOS/Colombia_2022_limpio.csv', index=False)  # Agregamos "index=False" para evitar que se guarde el índice en el archivo CSV.

import pandas as pd

#Importamos el archivo "Argentina_2022" desde nuestro Drive
Argentina_2022 = pd.read_csv('/content/drive/MyDrive/BASES DE DATOS/Argentina_2022.csv')

#Vemos las columnas que tiene nuestro csv
print(Argentina_2022.columns)

#Limpiamos la base de datos y quitamos las columnas que no son necesarias para la investigación del proyecto
Argentina_2022_limpio = Argentina_2022.drop(['uri', 'source', 'previous_rank'], axis=1)

#Guardamos nuestra base de datos limpia en nuestro Drive
Argentina_2022_limpio.to_csv('/content/drive/MyDrive/BASES DE DATOS/Argentina_2022_limpio.csv', index=False)  # Agregamos "index=False" para evitar que se guarde el índice en el archivo CSV.

import pandas as pd

#Importamos el archivo "Perú_2022" desde nuestro Drive
Perú_2022 = pd.read_csv('/content/drive/MyDrive/BASES DE DATOS/Perú_2022.csv')

#Vemos las columnas que tiene nuestro csv
print(Perú_2022.columns)

#Limpiamos la base de datos y quitamos las columnas que no son necesarias para la investigación del proyecto
Perú_2022_limpio = Perú_2022.drop(['uri', 'source', 'previous_rank'], axis=1)

#Guardamos nuestra base de datos limpia en nuestro Drive
Perú_2022_limpio.to_csv('/content/drive/MyDrive/BASES DE DATOS/Perú_2022_limpio.csv', index=False)  # Agregamos "index=False" para evitar que se guarde el índice en el archivo CSV.

import pandas as pd

#Importamos el archivo "Guatemala_2022" desde nuestro Drive
Guatemala_2022 = pd.read_csv('/content/drive/MyDrive/BASES DE DATOS/Guatemala_2022.csv')

#Vemos las columnas que tiene nuestro csv
print(Guatemala_2022.columns)

#Limpiamos la base de datos y quitamos las columnas que no son necesarias para la investigación del proyecto
Guatemala_2022_limpio = Guatemala_2022.drop(['uri', 'source', 'previous_rank'], axis=1)

#Guardamos nuestra base de datos limpia en nuestro Drive
Guatemala_2022_limpio.to_csv('/content/drive/MyDrive/BASES DE DATOS/Guatemala_2022_limpio.csv', index=False)  # Agregamos "index=False" para evitar que se guarde el índice en el archivo CSV.

import pandas as pd

#Importamos el archivo "Honduras_2022" desde nuestro Drive
Honduras_2022 = pd.read_csv('/content/drive/MyDrive/BASES DE DATOS/Honduras_2022.csv')

#Vemos las columnas que tiene nuestro csv
print(Honduras_2022.columns)

#Limpiamos la base de datos y quitamos las columnas que no son necesarias para la investigación del proyecto
Honduras_2022_limpio = Honduras_2022.drop(['uri', 'source', 'previous_rank'], axis=1)

#Guardamos nuestra base de datos limpia en nuestro Drive
Honduras_2022_limpio.to_csv('/content/drive/MyDrive/BASES DE DATOS/Honduras_2022_limpio.csv', index=False)  # Agregamos "index=False" para evitar que se guarde el índice en el archivo CSV.

import pandas as pd

#Importamos el archivo "México_2022" desde nuestro Drive
México_2022 = pd.read_csv('/content/drive/MyDrive/BASES DE DATOS/México_2022.csv')

#Vemos las columnas que tiene nuestro csv
print(México_2022.columns)

#Limpiamos la base de datos y quitamos las columnas que no son necesarias para la investigación del proyecto
México_2022_limpio = México_2022.drop(['uri', 'source', 'previous_rank'], axis=1)

#Guardamos nuestra base de datos limpia en nuestro Drive
México_2022_limpio.to_csv('/content/drive/MyDrive/BASES DE DATOS/México_2022_limpio.csv', index=False)  # Agregamos "index=False" para evitar que se guarde el índice en el archivo CSV.

import pandas as pd

#Importamos el archivo "España_2022" desde nuestro Drive
España_2022 = pd.read_csv('/content/drive/MyDrive/BASES DE DATOS/España_2022.csv')

#Vemos las columnas que tiene nuestro csv
print(España_2022.columns)

#Limpiamos la base de datos y quitamos las columnas que no son necesarias para la investigación del proyecto
España_2022_limpio = España_2022.drop(['uri', 'source', 'previous_rank'], axis=1)

#Guardamos nuestra base de datos limpia en nuestro Drive
España_2022_limpio.to_csv('/content/drive/MyDrive/BASES DE DATOS/España_2022_limpio.csv', index=False)  # Agregamos "index=False" para evitar que se guarde el índice en el archivo CSV.

import pandas as pd

#Importamos el archivo "Global_2022" desde nuestro Drive
Global_2022 = pd.read_csv('/content/drive/MyDrive/BASES DE DATOS/Global_2022.csv')

#Vemos las columnas que tiene nuestro csv
print(Global_2022.columns)

#Limpiamos la base de datos y quitamos las columnas que no son necesarias para la investigación del proyecto
Global_2022_limpio = Global_2022.drop(['uri', 'source', 'previous_rank'], axis=1)

#Guardamos nuestra base de datos limpia en nuestro Drive
Global_2022_limpio.to_csv('/content/drive/MyDrive/BASES DE DATOS/Global_2022_limpio.csv', index=False)  # Agregamos "index=False" para evitar que se guarde el índice en el archivo CSV.