funcionario = input("Digite o nome do funcionário")
valorhora = float(input("Digite o valor hora trabalhada R$"))
trab = float(input("Digite quantas horas trabalhadas"))

bruto = (valorhora*trab)
liquido = (bruto*9/100)
salario = (bruto-liquido)                
print("O Salário bruto é R$", bruto)
print("O Salário liquido é R$", salario)
