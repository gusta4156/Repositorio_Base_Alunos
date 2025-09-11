print("--------------------")
print("| SISTEMA DE PROVA |")
print("--------------------")
nome = input("nome do aluno:")
prova1 = float(input("nota da primeira prova"))
prova2 = float(input("nota da segunda prova"))
prova3 = float(input("nota da terceira prova"))
media = (prova1+prova2+prova3)/3
if media >=5:
    print("Aprovado")
else:
    print("reprovado")
print("--------------------")