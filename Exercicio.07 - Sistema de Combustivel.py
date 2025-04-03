tipo = input("Digite G para gasolina\n"
             "E digite E para etanol\n"
             "Qual o tipo? ")
litro = float(input("Digite a quantidade de litros de gasolina: "))

gasolina = 5.80
etanol = 4.90

if tipo == "G":
    valor = litro * gasolina
else:
    valor = litro * etanol

print(f"Valor a pagar: R${valor}")