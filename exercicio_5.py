def inverter_string(string):
  invertida = ""
  for i in range(len(string) - 1, -1, -1):
    invertida += string[i]
  return invertida

entrada = input("Digite uma string para ser invertida: ")

string_invertida = inverter_string(entrada)

print("String invertida:", string_invertida)