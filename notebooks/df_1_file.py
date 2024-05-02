import pandas as pd
import numpy as np

# guarda en variables los datasets y su fuente
df_1 = pd.read_csv(r'C:\Users\34690\Documents\THE BRIDGE\Repositorio\Repositorio_cambios_COPIA\2-Data_Analysis\Entregas\EDA_final\data\supermarket_sales - Sheet1.csv')

# Definir el diccionario de ciudades para realizar los cambios
cambio_ciudades = {'Naypyitaw': 'Madrid', 'Yangon': 'Santander', 'Mandalay': 'Valladolid'}

# Cambiar los valores en la columna 'City' utilizando el método replace()
df_1['City'] = df_1['City'].replace(cambio_ciudades)

# Cambiar el nombre de la columna 'cogs' a 'Sales Income'
df_1.rename(columns={'cogs': 'Sales Income'}, inplace=True)



df_1


