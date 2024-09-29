while True:
    try:
        horas = input("")
        if horas == "f":
            print("Fim...")
            break
        else: 
            if 0<=int(horas[:2]) < 12 and int(horas[:2])< 24 and int(horas[3:])<60 and horas[2]==":":
                angulohoras = int(horas[:2])*30
                angulomin = int(horas[3:])*6
                menorangulo = abs(angulohoras - angulomin)
                if menorangulo > 180 :
                    print (f"O menor ângulo é de {abs(360 - menorangulo)}°")
                else:
                    print (f"O menor ângulo é de {abs(menorangulo)}°")
            if int(horas[:2]) >= 12 and int(horas[:2])< 24 and int(horas[3:])<60 and horas[2]==":":
                angulohoras = (int(horas[:2])-12)*30
                angulomin = int(horas[3:])*6
                menorangulo = abs(angulohoras - angulomin)
                if menorangulo > 180 :
                    print (f"O menor ângulo é de {abs(360 - menorangulo)}°")
                else:
                    print (f"O menor ângulo é de {abs(menorangulo)}°")
            if int(horas[:2]) not in range(24):
                print ("Input Inválido")
                
    except Exception:
        print ("Input Inválido")
        
