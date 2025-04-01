nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
salario = float(input("Digite o seu salario: "))
aumento = int(input("Qual o percentual de aumento: "))
valorReal = salario * aumento/100
novoSalario = salario + valorReal

print(f"Olá {nome}, sua idade é: {idade}\n e o seu salario é: R${salario:.2f} e voce recebeu\n"
      f"1{valorReal:.2f} de aumento e seu novo salario é R${novoSalario:.2f}")
