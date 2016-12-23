def maximo(m,n):
  if m > n:
    x = m
  else:
    x = n
    
  return x  


def main():
  m = int(input("Escreva o primeiro inteiro: "))
  n = int(input("Escreva o segundo inteiro: "))
  
  print(maximo(m,n))
main()  
  
