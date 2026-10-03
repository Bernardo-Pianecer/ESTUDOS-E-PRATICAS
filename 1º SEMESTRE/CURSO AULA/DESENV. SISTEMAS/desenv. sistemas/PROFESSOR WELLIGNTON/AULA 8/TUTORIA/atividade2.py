vendas = [320, 450, 280, 510, 390, 480, 600,
        410, 350, 520, 470, 380, 540, 620,
        430, 490, 510, 580, 450, 600]

total = sum(vendas)

media = total / len(vendas)

maior = max(vendas)
menor = min(vendas)

contador = 0

for venda in vendas:
    if venda > media:
        contador += 1

melhor_dia = vendas.index(maior) + 1

dias_excelentes = []

for venda in vendas:
    if venda > 500:
        dias_excelentes.append(venda)

print(f"Total: R$ {total}")
print(f"Média: R$ {media:.2f}")
print(f"Maior: R$ {maior} • Menor: R$ {menor}")
print(f"Dias acima da média: {contador}")
print(f"Melhor dia: {melhor_dia} (R$ {maior})")
print(f"Dias excelentes: {dias_excelentes}")