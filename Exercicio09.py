num = int(input("Digite um número \n"
                "entre 1 e 12 : "))
if num < 1 or num > 12 :
    print("Valor inválido")
else:
    if num == 1:
        print("Janeiro")
    elif num == 2:
        print("Fevereiro")
    elif num == 3:
        print("Março")
    elif num == 4:
        print("Abril")
    elif num == 5:
        print("Maio")
    elif num == 6:
        print("Junho")
    elif num == 7:
        print("Julho")
    elif num == 8:
        print("Agosto")
    elif num == 9:
        print("Setembro")
    elif num == 10:
        print("Outubro")
    elif num == 11:
        print("Novembro")
    else :
        print("Dezembro")
