#Faça um programa  que leia um vetor de n elementos  e imprima os dois menores elementos.
#Entrada :  20 15 8 7 6  Saída: 6 7
#Entrada : 8 10 1 50 28 30  Saída: 1 8


#Leitura dos elementos do vetor
vet= list (map(int, input().split()))
#Inicializa o menor com primeiro elemento  e o sgeundo menor com o segundo 
menor = 0 
menor2= 1

for i in range(len(vet)):
    #Se o elemento i for o menor
    if vet[i]< vet[menor]:
        #menor é o i e o segundo menor é o menor 
        menor2=menor
        menor=i 
        #verifica se é o segundo menor
    elif vet[i]< vet[menor2]:
        menor2=i
print( vet[menor])
print (vet [menor2])         