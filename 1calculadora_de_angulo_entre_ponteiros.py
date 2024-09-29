while True:
    try:
        horas = input("")
        if horas == "f":
            print("Fim...")
            break
        else: 
            if int(horas[:2]) < 12 and int(horas[:2])< 24 and int(horas[3:])<60 and horas[2]==":":
                angulohoras = int(horas[:2])*30
                angulomin = int(horas[3:])*6
                menorangulo = angulohoras - angulomin
                if menorangulo > 180 :
                    print (f"O menor ângulo é de {360 - menorangulo}°")
                else:
                    print (f"O menor ângulo é de {menorangulo}°")
            if int(horas[:2]) >= 12 and int(horas[:2])< 24 and int(horas[3:])<60 and horas[2]==":":
                angulohoras = (int(horas[:2])-12)*30
                angulomin = int(horas[3:])*6
                menorangulo = angulohoras - angulomin
                if menorangulo > 180 :
                    print (f"O menor ângulo é de {360 - menorangulo}°")
                else:
                    print (f"O menor ângulo é de {menorangulo}°")
    except Exception:
        print ("Input Inválido")
