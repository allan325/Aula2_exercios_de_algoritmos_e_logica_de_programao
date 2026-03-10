quantidade = int(input("Quantas notas você quer informar:"))
notas = []
for i in range (quantidade):
  while True:
     nota = float(input("Digite a nota:"))
     if  0 <= nota  <=10 :
      notas.append(nota)
      break
     else:
          print("não pode esse numero")

total = sum(notas)
media = total / quantidade

print(f"Sua media final é {media}")