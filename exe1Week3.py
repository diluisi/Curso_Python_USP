import math

a = float(input("Insira o valor de a:"))
b = float(input("Insira o valor de b:"))
c = float(input("Insira o valor de c:"))

delta = b ** 2 - 4 * a * c

if delta >= 0:
  raiz1 = (-b + math.sqrt(delta))/(2 * a)
  raiz2 = (-b - math.sqrt(delta))/(2 * a)
  if raiz1 != raiz2:
    print("A raiz 1 é igual a", raiz1, "e a raiz 2 é igual a", raiz2)
  else:
    print("A raiz é igual a", raiz1)
else:
  print("Não tem raízes reais!")
