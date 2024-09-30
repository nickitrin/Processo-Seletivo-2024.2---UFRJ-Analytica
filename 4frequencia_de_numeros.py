dic={}
while True:
    numero = input("")
    if numero == "f":
        print("Fim...")
        break
    else:
        for i in dic:
            if numero == i :
                dic[i]+=1
        if numero not in dic:
            dic[numero]= 1
    print(dic.items())
