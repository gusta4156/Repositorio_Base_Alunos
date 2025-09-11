print("|-------------------")
print("|    calculadora    ")
print("--------------------")
print("|1-soma            |")
print("|2-subtração       |")
print("|3-multiplicação   |")
print("|4-divisão         |")
print("|-------------------")
opcoes = int(input("escolh uma das opções"))
numero1 = int(input("digite o primeiro múmero"))
numero2 = int(input("digite o segundonúmero"))

if opcoes == 1:
    print(numero1+numero2)
elif opcoes == 2:
    print(numero1-numero2)
elif opcoes == 3:
    print(numero1*numero2)
elif opcoes == 4:
    print(numero1/numero2)

else:
    print("digite uma opção valida!")