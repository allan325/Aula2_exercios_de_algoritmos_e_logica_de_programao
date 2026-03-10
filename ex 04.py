print("Soma apenas dos pares")

numero = int(input("Digite um numero:"))
soma =  0
for i in range (1,numero+1,) :
   if i %2 ==0 :
    soma += i
   
print(soma)