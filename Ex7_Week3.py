import math

def main():
  a = int(input("Insira o primeiro valor:"))
  b = int(input("Insira o primeiro valor:"))
  c = int(input("Insira o primeiro valor:"))
  d = int(input("Insira o primeiro valor:"))
  
  dist = math.sqrt((a - c)**2 + (b - d)**2)
  
  if dist >= 10:
    print("Longe")
  else:
    print("Perto")
  
main() 
