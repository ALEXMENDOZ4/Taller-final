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


dep_conta = data.groupby('Nombre departamento').count()
top_10_dep = dep_conta['ID'].sort_values(ascending=False).head(10)


print('\n28)')
array_dep = list(top_10_dep.keys())
only_10_dep = data[data['Nombre departamento'].isin(array_dep)]
groupby = ['Nombre departamento', 'Fecha de diagnóstico']
con_10_dep = only_10_dep.groupby(groupby)['ID'].count()


# contagiados
df_co_dep = con_10_dep.unstack(0).fillna(0)
df_co_dep.cumsum().plot(subplots=True, figsize=(14, 7), title='28)Contagiado')


# recuperados
groupby2 = ['Recuperado', 'Nombre departamento', 'Fecha de diagnóstico']
con_10_dep2 = only_10_dep.groupby(groupby2)['ID'].count()
df_co_depR = con_10_dep2['Recuperado'].unstack(0).fillna(0)
df_co_depR.cumsum().plot(subplots=True, figsize=(14, 7), title='28)Recuperado')


# fallecidos
df_co_depF = con_10_dep2['Fallecido'].unstack(0).fillna(0)
df_co_depF.cumsum().plot(subplots=True, figsize=(14, 7), title='28)Fallecido')
plt.show()
