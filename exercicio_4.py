# Dados de faturamenteo por cada Estado
faturamento = {
  'SP': 67836.43,
  'RJ': 36678.66,
  'MG': 29229.88,
  'ES': 27165.48,
  'Outros': 19849.53
}

# Total de faturamento por todos os Estados
faturamento_total = sum(faturamento.values())

# Percentuais de faturamento por Estado
percentuais = {estado: (valor / faturamento_total) * 100 for estado, valor in faturamento.items()}

# Resultado final
print("Percentuais de faturamento por Estado:")
for estado, percentual in percentuais.items():
  print(f"{estado}: {percentual:.2f}%")