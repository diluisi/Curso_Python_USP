def fizzbuzz(n):
  if (n % 3 == 0) and (n % 5 != 0):
    x = "Fizz"
  elif (n % 5 == 0) and (n % 3 != 0):
    x = "Buzz"
  elif (n % 5 == 0) and (n % 3 == 0):
    x = "FizzBuzz"
  else:
    x = n
    
  return x  


def main():
  n = int(input("Escreva um inteiro: "))
  print(fizzbuzz(n))
main()  
  
