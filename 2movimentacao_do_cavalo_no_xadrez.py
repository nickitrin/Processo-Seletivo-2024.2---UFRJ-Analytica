letras_casas= ["a","b","c","d","e","f","g","h"]
numeros_casas= list(range(1,9))
casos_possiveis = [[-1,-2], [-1,2], [-2,-1], [-2,1], [1,-2], [1,2], [2,-1], [2,1]]

while True:
    casa = input("")
    if casa == "f":
        print("Fim...")
        break
    else:
        letracasa_cavalo = letras_casas.index(casa[0])
        numerocasa_cavalo = numeros_casas.index(int(casa[1]))
        cavalo_casas_num=[]
        cavalo_casas=[]
        
        for i in casos_possiveis:
            if (letracasa_cavalo - i[0])>=0 and (numerocasa_cavalo - i[1])>=0:
                cavalo_casas_num+= [[letracasa_cavalo - i[0], numerocasa_cavalo - i[1] ]]
        print (cavalo_casas_num)
        
        for n in cavalo_casas_num:
            cavalo_casas+= [[letras_casas[n[0]] , numeros_casas[n[1]]]]
            print (cavalo_casas)

