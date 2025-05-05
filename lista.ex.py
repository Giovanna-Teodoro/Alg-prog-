#Faça um programa que leia um vetor de n elementos e em seguida leia um inteiro x. Por fim, seu programa deve multiplicar todos os elementos do vetor por x
#Entrada 20 2 5 3  SAída : 40 4 10 6
#ENtrada  15 5 2 8 7  Saída: 70 25 10 40 35


#Leitura dos elementos do vetor

vetor= list(map(int,input().split()))

#leitura do valor de n ou X 

nu= int(input())

for i in range(len(vetor)):
    vetor[i]=nu*vetor[i]
#impressão do vetor  
for i in range(len(vetor)):
    print(vetor[i], end=" ")    