nota1 = float(input("Primeira nota"))
nota2 = float(input("Segunda nota"))
nota3 = float(input("Terceira nota"))
mediaNota = (nota1 + nota2 + nota3 )/3

if mediaNota >= 7:
    print(f"Média: {mediaNota:.2f}, Aprovado!")
else:
    if mediaNota < 4:
        print(f"Média: {mediaNota:.2f}, Reprovado!")
    else:
        print(f"Média: {mediaNota:.2f}, Recuperação!")
