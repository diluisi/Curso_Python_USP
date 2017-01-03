
def maximo(m,n,o):
  if (m > n) and (n > o):
    x = m
  elif (n > m) and (m > o):
    x = n
  else:
    x = o
  return x  


def main():
  m = int(input("Escreva o primeiro inteiro: "))
  n = int(input("Escreva o segundo inteiro: "))
  o = int(input("Escreva o terceiro inteiro: "))
  
  print(maximo(m,n,o))
main() 
