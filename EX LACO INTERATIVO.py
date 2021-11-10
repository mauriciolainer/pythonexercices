RESP="S"
while RESP == "S" or RESP == "s":
    n = int(input("Digite o n"))
    r = n *2
    print("Resultado: " ,r)
    RESP = str(input("Deseja continuar? n "))
