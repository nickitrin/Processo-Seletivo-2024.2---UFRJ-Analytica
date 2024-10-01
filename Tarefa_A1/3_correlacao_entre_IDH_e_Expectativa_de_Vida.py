import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("arquivo.csv")

# grafico “Scatter Plot”, IDH x Expectativa de Vida.

df_idhm = df.loc[:,'idhm']
df_exp_de_vida = df.loc[:,'expectativa_vida']


plt.scatter(df_idhm, df_exp_de_vida)
plt.show()

print("\n De acordo com o gráfico, quanto maior o IDHM maior a expectativa de vida, e além disso menor a discrepancia \n de expectativa de vida, por exemplo, no intervalo IDHM 0.3-0.4 há uma variação em relação à média de expectativa de vida \n muito maior do que no intervalo IDHM 0.7-0.8 ")
