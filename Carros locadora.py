modelo = str(input("Informe o modelo do carro"))
qtde_estoque = int(input("Informe a quantidade de carros em estoque"))
qtde_alugada = int(input("Informe a quantidade de carros alugada"))
vr_locacao = float(input("Informe o valor da locação"))
saldo_carros = qtde_estoque-qtde_alugada
vr_total = qtde_alugada*vr_locacao
print("Saldo de carros na locadora", saldo_carros)
print("Valor total", vr_total)


                       
