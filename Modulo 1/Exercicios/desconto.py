preco = float (input("qual o preço do produto?"))
porcentagem = float (input("qual a porcentagem de desconto?"))
desconto = preco * (porcentagem / 100)
print(f"o produto que custa R${preco} terá R${desconto} de desconto")
