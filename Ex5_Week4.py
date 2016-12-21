def primo(n):
  ans = True
  for i in range(2,n):
    if(n % i == 0):
      ans = False 
  return(ans)
  
def main():
  n = int(input("Insira o valor a ser verificado: "))
  print(primo(n))
main() 
