
palavra = input("Digite uma palavra:")
contador = 0
vogais = "aeiouAEIOU"
quantidade_vogais = []

for letra in palavra :
    if letra in vogais:
        quantidade_vogais.append(letra)
        contador +=1
   

print(f"Tem {contador} vogais e são {quantidade_vogais} ")