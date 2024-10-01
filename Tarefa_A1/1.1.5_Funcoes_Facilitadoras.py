import numpy as np

array1 = np.array([5.5, 3.8, 9, 7.5, 10.0, 9.9, 8.5])


# Ordene os elementos do array da questão anterior usando o método .sort() próprio do numpy.

array1=np.sort(array1)

print (array1)

#Para saber as dimensões do array podemos use a propriedade .shape

print (array1.shape)

#Extraia a média de um array numpy utilizando o metodo .mean():

print(np.mean(array1))

#O mesmo pode ser feito para o desvio padrao, com .std(), maxima e mınima com .max() e .min(), alem de muitos outros metodos.

print (np.std(array1))
print (np.max(array1))
print (np.min(array1))

# Gere um array de 100 numeros aleatorios entre 0 e 10 (inclusive) e imprima na tela a media, desvio padrao, o maior valor e o menor valor.

from numpy import random

array_de_100 = random.rand(100)*10

print(array_de_100)

print (np.mean(array_de_100))
print (np.std(array_de_100))
print (np.max(array_de_100))
print (np.min(array_de_100))
