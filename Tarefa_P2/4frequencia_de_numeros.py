dic={}
while True:
    numero = input("")    
    if numero == "f":
        break
        
    try:
        if isinstance(int(numero), int):
            for i in dic:
                if numero == i :
                    dic[i]+=1
            if numero not in dic:
                dic[numero]= 1
                
    except Exception:
        pass

for i in dic:
    if dic[i]!=1:
        print("O número", i, "apareceu", dic[i], "vezes")
    else:
        print("O número", i, "apareceu", dic[i], "vez")
print("Fim...")
