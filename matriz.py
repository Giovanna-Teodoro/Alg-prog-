#Leitura da quantidade de linhas da matriz
n=int(input())

matriz=[]

#Para cad auma das linhas faça a leitura 
for i in range(n):
    linha=[]
    linha= list(map(int,input().split()))

    matriz.append(linha)

#IMprime de diversas formas a matriz
for i in range(n):
    print(matriz[i])

for i in range (n):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=" ")
    print()        


soma=0

for  i in range (n):
    for j in range(len(matriz[i])):
        soma+=matriz[i][j]

print(soma)        