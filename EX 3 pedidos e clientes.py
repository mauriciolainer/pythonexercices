i = 1
while i <= 3:
    codigo =int(input("Digite o código"))
    descricao =str(input("Digite a descrição"))
    prunitario =float(input("Digite o preço unitário"))
    quantidade = int(input("Digite a quantidade"))
    total = prunitario * quantidade
    if total>= 100:
        desconto = total * 0.1
    else:
        desconto = total * 0.05
    totalcompra = total - desconto
    print("Desconto", desconto)
    print("Valor total", totalcompra)
    i=i+1
