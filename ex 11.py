numero = input("Digite um número inteiro positivo: ")

soma = 0

for digito in numero:
    soma += int(digito)

print("A soma dos dígitos é:", soma)