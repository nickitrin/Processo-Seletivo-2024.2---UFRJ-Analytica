dp2=0
contador = 1

for i in array1:
    dp2 = (i-media)**2+dp2
    dp= (dp2/contador)**0.5
    contador+=1
print (dp)
