quantidade = int(input("Quantos números você quer digitar:"))

numero =  int(input("Digite quias números você quer comparar:"))
     
maior = numero
menor = numero

for i in range (quantidade-1):
    numero =  int(input("Digite quias números você quer comparar:"))
     
    if numero > maior :
        maior = numero
    elif numero < menor:
        menor = numero  

print (f"o maior numero é {maior}")
print (f"o menor numero é {menor}")