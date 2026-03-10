numero = int(input("digite um numero:"))
if numero > 1:
 for i in range (2,numero) :
    if numero %i == 0:
        print(f"O numero {numero} não é primo.")
        break
 else :
  print(f"O numero {numero} é primo.")
else :
  print("Numeros primo começa a partir de 2")