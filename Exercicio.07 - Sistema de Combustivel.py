tipo = input("Digite G para gasolina\n"
             "E digite E para etanol\n"
             "Qual o tipo? ")
litro = float(input("Digite a quantidade de litros de gasolina: "))

gasolina = 5.80
etanol = 4.90

if tipo == "G" or tipo == "g":
    valor = litro * gasolina
elif tipo == "E" or tipo == "e":
    valor = litro * gasolina
else:
    print("Tipo invalido, tente novamente")

print(f"Valor a pagar: R${valor:.2f}")
