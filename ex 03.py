print("Contagem de pares e ímpares")

numero = int(input("Digite um numero: "))
pares = 0
impares = 0

for i in range(1, numero + 1):
   
    if i % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Tem {impares} numeros ímpares.")
print(f"Tem {pares} numeros pares.")