import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#grafico_freq_idh_1991

filtro91 = df["ano"] == 1991
df_filtrado91 = df[filtro91]


df_filtrado91 = df[filtro91]

grafico_uf_filtrado91 = df_filtrado91.loc[:,'idhm']
plt.hist(grafico_uf_filtrado91, 5, rwidth=0.9)
plt.show()

#grafico_freq_idh_2000

filtro00 = df["ano"] == 2000
df_filtrado00 = df[filtro00]


df_filtrado00 = df[filtro00]

grafico_uf_filtrado00 = df_filtrado00.loc[:,'idhm']
plt.hist(grafico_uf_filtrado00, 5, rwidth=0.9)
plt.show()


#grafico_freq_idh_2010

filtro10 = df["ano"] == 2010
df_filtrado10 = df[filtro10]


df_filtrado10 = df[filtro10]

grafico_uf_filtrado10 = df_filtrado10.loc[:,'idhm']
plt.hist(grafico_uf_filtrado10, 5, rwidth=0.9)
plt.show()
