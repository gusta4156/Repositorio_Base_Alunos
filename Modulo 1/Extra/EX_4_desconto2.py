# Faça uma atualização no código do exercício anterior, agora o programa deve exibir o nome do produto, o valor do desconto e o valor final do produto.

# OUTPUT ESPERADO:

# Produto: FIAT TORO
# Preço: 200000
# Porcentagem de desconto: 15
# O FIAT TORO com 15.0% de desconto custará R$ 170000.0

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
produto = input("produto: ")
preco = float(input("preço: "))
porcentagem = float(input("porcentagem de desconto: "))
valor_desconto = float(preco*(porcentagem/100))
print(f"o {produto} com {porcentagem} % de desconto custará {preco-valor_desconto}")


