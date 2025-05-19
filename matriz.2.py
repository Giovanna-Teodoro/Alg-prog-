#Faça um programa que leia o número de linhas e colunas de uma matriz . Em seguida  leia n linhas contendo m colunas cada e calcule o maior elemento da matriz

#Ex  ENTRADA       SAÍDA
#2 3                  15    
# 1 5 7
#5 3 8                   

matriz=[]

line=int(input())

for i in range(line):
    linha=[]
    linha=list(map(int,input().split()))
    matriz.append(linha)
auxiliar=0
maior=0
for j in range (len(matriz)):
    for k in range(len(matriz[j])):
        auxiliar= matriz[j][k]
        if auxiliar > maior:
            maior=auxiliar
print(maior)  





  

