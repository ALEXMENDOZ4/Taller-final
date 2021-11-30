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




mun_conta = data.groupby('Nombre municipio').count()
top_10_mun = mun_conta['ID'].sort_values(ascending=False).head(10)


print('\n29)')
array_mun = list(top_10_mun.keys())
only_10_mun = data[data['Nombre municipio'].isin(array_mun)]
groupby = ['Nombre municipio', 'Fecha de diagnóstico']
con_10_mun = only_10_mun.groupby(groupby)['ID'].count()


# contagiados
df_co_mun = con_10_mun.unstack(0).fillna(0)
df_co_mun.cumsum().plot(subplots=True, figsize=(14, 7), title='29)Contagiado')


# recuperados
groupby2 = ['Recuperado', 'Nombre municipio', 'Fecha de diagnóstico']
con_10_mun2 = only_10_mun.groupby(groupby2)['ID'].count()
df_co_munR = con_10_mun2['Recuperado'].unstack(0).fillna(0)
df_co_munR.cumsum().plot(subplots=True, figsize=(14, 7), title='29)Recuperado')


# fallecidos
df_co_munF = con_10_mun2['Fallecido'].unstack(0).fillna(0)
df_co_munF.cumsum().plot(subplots=True, figsize=(14, 7), title='29)Fallecido')
plt.show()