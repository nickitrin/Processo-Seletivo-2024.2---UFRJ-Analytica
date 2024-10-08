import pandas as pd
import numpy as np

# A partir do valor de media filtre o dataframe dos dados de 1991 para apenas os que possuem IDH maior que a media.

print ("\n Dataframe dos dados de 1991 que possuem IDH maior que a media \n")

df = pd.read_csv("arquivo.csv")

filtro = df["ano"] == 1991
df_filtrado = df[filtro]

df_idhm = df_filtrado.loc[:, 'idhm']

filtroidhmmaior =  df['idhm'] > np.mean(df_idhm) 

df_filtrado = df[ filtro & filtroidhmmaior ]

print (df_filtrado)

#Retorne os estados referentes a essas linhas resultantes.

print ("\n Estados que estao acima da media \n")
print(df_filtrado.loc[:,'sigla_uf'])

# Ordene os dados do DataFrame de 1991 de acordo com o IDH

print ("\n Dados do DataFrame de 1991 de acordo com o IDH \n")
newdf = df_filtrado.sort_values(by='idhm')

print(newdf)

# Mostre a tabela dos 5 primeiros 

print ("\n Tabela dos 5 primeiros de acordo com o IDH \n")
print(newdf.head(5))

# Analise os dados de IDH. Use as funcoes de .min(), .max(), .idxmin() e .idxmax() para saber qual o estado de maior e menor IDH no DataFrame do ano de 1991.

df_filtroidhm_max= df[df['idhm'] == np.max(df_idhm)] 
df_filtroidhm_min= df[df['idhm'] == np.min(df_idhm)]
df_filtroidhm_idxmax= df.idxmax()
df_filtroidhm_idxmin= df.idxmin()

print ("\n Estado de maior IDH no DataFrame do ano de 1991 foi o Distrito Federal de acordo com:  \n")
print(df_filtroidhm_max.loc[:, 'sigla_uf'])

print(df_filtroidhm_idxmax)

print ("\n Estado de menor IDH no DataFrame do ano de 1991 foi o Maranhao de acordo com: \n")
print(df_filtroidhm_min.loc[:, 'sigla_uf'])

print(df_filtroidhm_idxmin)
