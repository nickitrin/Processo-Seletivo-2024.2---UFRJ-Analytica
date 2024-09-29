l=[100,50,20,10,5,2]
lx=["100.00","50.00","20.00","10.00","5.00","2.00"]
v=(float(input()))

i=0
print("NOTAS:")
while i<=len(l)-1:
    valor=v//l[i]
    v=v%l[i]
    i+=1
    print (int(valor),"nota(s) de R$",lx[i-1])

l2=[100,50,25,10,5,1]
l3=["1.00","0.50","0.25","0.10","0.05","0.01"]

v=round(v%2*100,2)
i=0
print("MOEDAS:")
while i<=len(l2)-1:
    valor=v/l2[i]
    v=v%l2[i]
    i+=1
    print (int(valor),"moeda(s) de R$",l3[i-1])
