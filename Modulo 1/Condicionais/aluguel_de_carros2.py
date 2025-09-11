modelo = input("qual foi o modelo do carro alugado?")
dias = int(input("Quantos dias o carro foi alugado?"))
km = int(input("Quantos km o carro rodou?"))
total_dias=(dias*60)
total_km=(km*0.15)
valor_total = (dias+km)
if modelo == "mustang":
    diaria = 60
else:    
    modelo = "golf"
    diaria =50
total_dias=(dias*diaria)
total_km=(km*0.15)
valor_total = (dias+km)
print(f"você alugou o {modelo} e rodou {km} km por {dias}.o valor total a pagar é R${valor_total}")