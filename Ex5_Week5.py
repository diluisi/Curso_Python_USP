def vogal(str):
  mylist = [65, 69, 73, 79, 85, 97, 101, 105, 111, 117]
  if str not in mylist:
    return "Consoante"
  else:
    return "Vogal"
    

def main():
  str = ord(input("Insira uma letra: "))
  print(vogal(str))
main() 
