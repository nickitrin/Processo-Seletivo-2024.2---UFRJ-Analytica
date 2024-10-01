import numpy as np

array1 = np.array([5.5, 3.8, 9, 7.5, 10.0, 9.9, 8.5])

#Calcule a media dos valores usando iteracao.

contador = 1
soma = 0 

for i in array1:
    soma+=i
    media= soma/contador
    contador+=1

print (media)

# Calcule o desvio padrao dos valores usando iteracao

dp2=0
contador = 1

for i in array1:
    dp2 = (i-media)**2+dp2
    dp= (dp2/contador)**0.5
    contador+=1
print (dp)
