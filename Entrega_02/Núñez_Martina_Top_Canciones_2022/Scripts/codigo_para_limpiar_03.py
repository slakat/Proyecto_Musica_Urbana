# -*- coding: utf-8 -*-
"""ENTREGA 02 - NGN. 03

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10MYKj0QunVl2O0kL-W2cub1P8RzagZB7

Identificar cuáles de los siguientes artistas urbanos chilenos: "Pailita", "Polimá Westcoast", "Paloma Mami", "Cris Mj", "Ak4:20" y "Marcianeke", son los más escuchados dentro de los países seleccionados en la plataforma de Spotify.
"""

import pandas as pd

#Cargamos el archivo CSV en un DataFrame.
Base_de_datos_original = pd.read_csv('/content/drive/MyDrive/BASES DE DATOS/BASE DE DATOS ORIGINAL 2022.csv')

#Lista de nombres de los artistas urbanos chilenos que deseamos buscar.
nombres_artistas_urbanos_chilenos = ["Pailita", "Polimá Westcoast", "Paloma Mami", "Cris Mj", "Ak4:20", "Marcianeke"]

#Creamos una condición que busca cualquiera de los nombres de artistas urbanos chilenos en la columna "artist_names".
#Usamos el operador | (OR) para combinar las condiciones de búsqueda de todos los nombres de artistas urbanos chilenos especificados en la lista nombres_artistas_urbanos_chilenos.
#La opción "case=False" indica que la búsqueda no distinga entre mayúsculas y minúsculas, y "na=False" evita que se traten los valores nulos.
condicion = Base_de_datos_original["artist_names"].str.contains('|'.join(nombres_artistas_urbanos_chilenos), case=False, na=False)

#Filtramos el DataFrame utilizando la condición.
resultados = Base_de_datos_original.loc[condicion]

#Ordenamos el DataFrame por la columna "país" y las otras columnas especificadas.
resultados_ordenados = resultados.sort_values(by=["país", "rank", "artist_names", "track_name", "peak_rank", "weeks_on_chart", "streams"])

#Guardamos el DataFrame procesado en un archivo CSV en nuestro Drive.
ruta_guardado = '/content/drive/MyDrive/BASES DE DATOS/base_de_datos_limpia.csv'
resultados_ordenados.to_csv(ruta_guardado, index=False)

"""Basándonos en el proceso de limpieza que llevamos a cabo anteriormente, procederemos a evaluar si podemos responder algunas preguntas cruciales para nuestra investigación a través de la base de datos."""

import pandas as pd

#Cargamos el archivo CSV
base_de_datos_limpia = '/content/drive/MyDrive/BASES DE DATOS/base_de_datos_limpia.csv'
data = pd.read_csv(base_de_datos_limpia)

#Mostrar las primeras 5 filas del DataFrame
primeras_filas = data.head()
print(primeras_filas)

#¿Cuál es el artista con más canciones en el ranking?
artista_con_mas_canciones = resultados_ordenados['artist_names'].value_counts().idxmax()
print(artista_con_mas_canciones)

#¿Cuál es el artista con más streams totales en todas sus canciones?
artista_con_mas_streams_totales = resultados_ordenados.groupby('artist_names')['streams'].sum().idxmax()
print(artista_con_mas_streams_totales)

#¿Cuál es el promedio de semanas en el chart para las canciones de cada artista?
promedio_semanas_por_artista = resultados_ordenados.groupby('artist_names')['weeks_on_chart'].mean()
print(promedio_semanas_por_artista)