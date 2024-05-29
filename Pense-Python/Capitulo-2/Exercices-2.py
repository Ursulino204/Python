preco_capa = 24.95
desconto = 0.40
preco_transport_first_copy = 3.00
preco_transport_additional_copy = 0.75

quantidade_copias = int(input("Digite a quantidade de cópias desejadas: "))

# Calculando o preço com desconto
preco_com_desconto = preco_capa - (preco_capa * desconto)

# Calculando o custo total de transporte
custo_transport = preco_transport_first_copy + max(quantidade_copias - 1, 0) * preco_transport_additional_copy

# Calculando o custo total de atacado
custo_total_atacado = quantidade_copias * preco_com_desconto + custo_transport

print("O custo total de atacado para {} cópias é: R$ {:.2f}".format(quantidade_copias, custo_total_atacado))
