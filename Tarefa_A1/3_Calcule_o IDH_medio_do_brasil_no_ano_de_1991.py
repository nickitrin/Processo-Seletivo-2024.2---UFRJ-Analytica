import pandas as pd

import numpy as np


df = pd.read_csv("arquivo.csv")

filtro = df["ano"] == 1991
df_filtrado = df[filtro]

df_idhm = df_filtrado.loc[:, 'idhm']

df_idhm = pd.to_numeric(df_idhm, errors='coerce')
df_idhm = df_idhm.dropna()

print (df_idhm)
print (np.mean(df_idhm))
