def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

def main():
  
  n = int(input("Digite um número: "))
  print(sum_digits(n))
  
main()
