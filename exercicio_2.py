numero = int(input("Digite um número inteiro: "))

a = 0;
b = 1;

encontrado = False;

while a <= numero:
  if a == numero:
    encontrado = True;
    break;

  a, b = b, a + b;

if encontrado:
  print(f"O número {numero} é um número de Fibonacci.")

else:
  print(f"O número {numero} não é um número de Fibonacci.")