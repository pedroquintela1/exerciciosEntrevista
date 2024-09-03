import json

# Aqui estamos carregando os dados de faturamento informados no arquivo JSON
with open("exercicio_3.json", "r") as file:
  faturamento_diario = json.load(file)

# Inicializando as variáveis
menor_faturamento = float('inf')
maior_faturamento = float('-inf')
soma_faturamento = 0
dias_com_faturamento = 0

# Percorrendo sobre os dados para encontrar o menor, maior e somar os faturamentos
for registro in faturamento_diario:
  valor = registro["faturamento"]

  if valor > 0:
    if valor < menor_faturamento:
      menor_faturamento = valor

    if valor > maior_faturamento:
      maior_faturamento = valor

    soma_faturamento += valor
    dias_com_faturamento += 1

media_mensal = soma_faturamento / dias_com_faturamento;

# Calculando os dias com faturamento acima da média
dias_acima_media = 0
for registro in faturamento_diario:
  valor = registro["faturamento"]
  if valor > media_mensal:
    dias_acima_media += 1

# Imprimindo os resultados
print(f"Menor faturamento: R${menor_faturamento:.2f}")
print(f"Maior faturamento: R${maior_faturamento:.2f}")
print(f"Média mensal: R${media_mensal:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")