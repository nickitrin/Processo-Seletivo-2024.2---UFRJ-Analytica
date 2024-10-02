
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("arquivo.csv")

filtro = df["ano"] == 1991
df_filtrado = df[filtro]



df_filtrado = df[filtro]

grafico_uf_filtrado = df_filtrado.loc[:,'sigla_uf']
grafico_pop_filtrado = df_filtrado.loc[:,'populacao_urbana']

plt.bar(grafico_uf_filtrado,grafico_pop_filtrado, width = 0.3)


plt.show()
