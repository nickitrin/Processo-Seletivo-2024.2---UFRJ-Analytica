import pandas as pd

import numpy as np


df = pd.read_csv("arquivo.csv")

filtro = df["ano"] == 1991
df_filtrado = df[filtro]

df_idhm = df_filtrado.loc[:, 'idhm']


print (df_idhm)
print (np.mean(df_idhm))

