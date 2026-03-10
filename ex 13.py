base = int(input("Digite o número base: "))
limite = int(input("Digite o limite: "))

for i in range(1, limite + 1):
    if i % base == 0:
        print(i)