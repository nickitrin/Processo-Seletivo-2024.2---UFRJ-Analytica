import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_csv("arquivo.csv")

# Utilizando a mesma base de dados, obtenha a diferenca de expectativa de vida de cada estado entre os anos de 1991 e 2010
filtro = df["ano"] == 1991
df_filtrado = df[filtro]
df_filtrado = df_filtrado.loc[:, 'expectativa_vida']


filtro2 = df["ano"] == 2010
df_filtrado2 = df[filtro2]

df_filtrado2 = df_filtrado2.loc[:, 'expectativa_vida']
df_diferenca= df_filtrado2.values - df_filtrado.values


filtro3 = df["ano"] == 1991
df_uffiltrado = df[filtro3]
dfdo_filtrodeuf = df_uffiltrado.loc[:, 'sigla_uf']



# Faca um grafico de barras com esses valores. 

print("\n diferenca de expectativa de vida de cada estado entre os anos de 1991 e 2010 \n")


plt.bar(dfdo_filtrodeuf,df_diferenca, width = 0.3)
plt.show()

#Retorne todos os estados que tiveram um aumento de pelo menos 10 anos na expectativa de vida entre 1991 e 2010.

df_diferenca_uf_exp_vida = pd.DataFrame({
    'sigla_uf':dfdo_filtrodeuf,
    'diferenca_exp_de_vida_1991-2010': df_diferenca
    
})


print("\n estados que tiveram um aumento de pelo menos 10 anos na expectativa de vida entre 1991 e 2010 \n") 

filtroexpvidamaior =  df_diferenca_uf_exp_vida['diferenca_exp_de_vida_1991-2010'] >= 10
df_diferenca_uf_exp_vida_maior = df_diferenca_uf_exp_vida [filtroexpvidamaior]
print(df_diferenca_uf_exp_vida_maior['sigla_uf'])


