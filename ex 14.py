quantidade = int(input("Quantos números você quer digitar:"))
numero =  int(input("Digite quias números você quer comparar:"))
maior = numero
menor = numero
numero1 = [numero]
positivos = 0
negativos = 0
zeros = 0

if numero > 0:
     positivos += 1
elif numero < 0:
     negativos += 1
else:
    zeros += 1

for i in range (quantidade-1):
     numero = float(input("Digite a nota:"))
     numero1.append(numero)
     if numero > maior :
        maior = numero
     elif numero < menor:
        menor = numero  
     if numero > 0:
        positivos += 1
     elif numero < 0:
        negativos += 1
     else:
        zeros += 1

total = sum(numero1)
media = total / quantidade
print(f"A soma total é {total}.")
print(f"Sua media final é {media}.")
print (f"o maior numero é {maior}.")
print (f"o menor numero é {menor}.")
print (f"tem {positivos} numeros positivo.")
print (f"tem {negativos} numeros negativos")
print (f"tem {zeros} numeros zeros")
