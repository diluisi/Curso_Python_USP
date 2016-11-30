def main():
  num_str = input("Digite um número inteiro: ")
  numbers = [int(i) for i in str(num_str)]
  s = numbers[-2:-1]
  print(s)
main()  
