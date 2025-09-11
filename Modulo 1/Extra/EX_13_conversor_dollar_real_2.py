# Atualize o código do exercício de conversor de dollar para real. Agora um "MENU" de opções aparecerá na tela pedindo ao usuário que escolha se quer converter
# de Reais para Dollar ou Dollar para reais. O usuário deve digitar a opção antes de informar os valores.

# OUTPUT ESPERADO:

#------- Exemplo 1 (Dólares para Reais):

# Escolha uma opção: 
# 1 - Dollar para Real
# 2 - Real para dollar
# Digite a opção: 1
# Informe a cotação atual do Dollar: 5.65
# Informe a quantidade de dólares: 150 
# O valor em reais é R$847.50

#---------- Exemplo 2 (Reais para Dólares)

# Escolha uma opção: 
# 1 - Dollar para Real
# 2 - Real para dollar
# Digite a opção: 2
# Informe a cotação atual do Dollar: 5.65
# Informe a quantidade de reais: 150
# O valor em dólares é $26.55

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
print("Escolha uma opção: ")
opcao1 = print("1 - dollar para real")
opcao2 = print("2 - real para dollar")
opcao = input("digite a opção: ")
atual_dollar = float(input("informe a quantidade de dóllares: "))
quantidade_dollar = float(input("informe a quantidade de dóllares: "))
print(F"O valor em reais é R${atual_dollar * quantidade_dollar}")

print("escolha uma opção: ")
opcao1 = print("1 - dollar para real")
opcao2 = print("2 - real para dollar")
opcao = input("digite a opção: ")
atual_dollar = float (input("informe a cotação atual do dollar: "))
quantidade_reais = float(input("informe a quantidade de reais: "))
print(F"o valor em reais é R${atual_dollar * quantidade_reais }")





