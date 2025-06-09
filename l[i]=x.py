#Faça um programa que leia um valor T e um inteiro N e, em seguida,
#preencha um vetor de n elementos com a sequência de valores de 0 até T-1
#repetidas vezes, até chegar em n elmentos.
#Em seguida, seu programa deve gerar o vetor de n elementos.

#Entrada: a entrada contém dois inteiros T e n,
#indicando o valor a ser usado nas sequências e o tamanho da lista a ser gerada.

#Saída: a saída deve ser uma lista no formato "L[i] = x", na qual i a
#posição do elemento na lista e x é o valor dele.

#Leitura dos valores T e N

T, N = map(int,input().split())

vetor=[] # declaração do vetor

#inicializa valor a preencher
valor=0

for i in range(N):
    for j in range(T):
        vetor.append(valor)
#Incementa o valor
        valor+=1
#Se o valor chegar no T, zera o mesmo
        if valor == T:
            valor=0
#Impressão 
for k in range(len(vetor)):
    print(vetor[k], end=" ")
    