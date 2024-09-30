#questão a

import numpy as np

array1 = np.array([5.5, 3.8, 9, 7.5, 10.0, 9.9, 8.5])

contador = 1
soma = 0 

for i in array1:
    soma+=i
    media= soma/contador
    contador+=1

print (media)

#questão b
