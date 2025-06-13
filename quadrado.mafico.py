#entrada da dimensão d amatriz
nu=int(input())
#declara a matriz e lista com a soma das linhas e colunas
matriz=[]
lista_soma=[]
soma=0
coluna=0
lista_coluna=[]
#leitura dos valores da matriz
for i in range(nu):
    matriz.append(list(map(int,input().split())))
#realiza a soma das colunas e a soma das linhas da coluna
for k in range(len(matriz)):
    for l in range (len(matriz[k])):
        soma+=matriz[k][l]
        coluna+=matriz[l][k]
    lista_soma.append(soma)
    lista_coluna.append(coluna)
    soma=0
    coluna=0
#soma das diagonais     
diagonal=0
lista_diagonal=[]
for i in range(nu):
    # Em cada linha, vai até o elemento da diagonal principal
    for j in range(i+1):
        diagonal+=matriz[i][j]
    lista_diagonal.append(diagonal) 
    diagonal=0
    
#comparação das somas
magico= True
aux=0

for j in range(len(lista_soma)):
    if lista_soma[j]==lista_coluna[j] and lista_soma[j] == lista_diagonal[j]:
        magico= True
    else:
        magico= False
        aux+=1
if magico == True and aux==0 :
    print(lista_soma[0])
else:
    print("-1")

