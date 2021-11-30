import pandas as pd
import matplotlib.pyplot as plt


url = 'covid_22_noviembre.csv'
data = pd.read_csv(url)

data.rename(columns={'ID de caso': 'ID'}, inplace=True)
# tratando los datos
data['Ubicación del caso'].replace('CASA', 'Casa', inplace=True)
data['Recuperado'].replace('fallecido', 'Fallecido', inplace=True)
data['Tipo de contagio'].replace('relacionado', 'Relacionado', inplace=True)
data['Tipo de contagio'].replace('RELACIONADO', 'Relacionado', inplace=True)
data['Tipo de contagio'].replace('EN ESTUDIO', 'En estudio', inplace=True)
data['Tipo de contagio'].replace('En Estudio', 'En estudio', inplace=True)
data['Sexo'].replace('m', 'M', inplace=True)
data['Sexo'].replace('f', 'F', inplace=True)



fallecidas = data[data['Ubicación del caso'] == 'Fallecido']
recuperados = data[data['Recuperado'] == 'Recuperado']

print('\n22)')
tasa_mortalidad = (len(fallecidas) / len(data)) * 100
tasa_recuperacion = (len(recuperados) / len(data)) * 100
print('tasa de mortalidad: ' + "{:.6f}".format(tasa_mortalidad))
print('tasa de recuperación: ' + "{:.6f}".format(tasa_recuperacion))