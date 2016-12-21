def verif_dig(n):
  dig1 = 0
  dig2 = 0
  verif = False

  while n != 0 and verif == False:
    dig1 = (n % 10)
    n = n//10
    dig2 = (n % 10)
    n = n//10
    
    if(dig1 == dig2):
      verif = True
    else:
        n = (n*10) + dig2

  return(verif)
  
def main():
  n = int(input("Insira o valor a ser verificado: "))
  print(verif_dig(n))
main()  
