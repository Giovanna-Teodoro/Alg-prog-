#Faça um programa que leia as vendas de n filias de uma loja durante m dias e determine.
# a) A soma das vendas em cada filiar.
# b) A soma das  vendas em cada dia de toda a rede.
# c) A filial que mais vendeu considerando o período todo.
# d) O dia de melhor venda da rede,  considerando a venda diária de todos as filias
# e) A filial e o fia do período que ocorreu a menor venda de todas, considerando as vendas individuais de todo o período
# Utilize as seguintes funções:
# def Soma_linhas(matriz, n), que recebe uma matriz , o número de linhas da mesmo e devolva a soma de cada linha.
# b) def Soma_Colunas(matriz,n), que recebe uma matriz  o número de linhas e devolve  a soma das colunas.
# c) Calcula_Maior(lista), que recebe uma lista e devolve o índice do maior elemento.
#d) def, Calcula_Maior_Matriz(materiz, n), que recebe uma matriz, o número d elinhas e devolve a linha e a coluna do maior elemento.

#Função para ler a matriz
def Le_Matriz(mat,linhas):
    #Para cada uma das linhas da Matriz
    for i in range(linhas):
        lin=list(map(int,input().split()))
        mat.append(lin)
#função que imprime uma lista
def Imprime_Lista(lista):
    for i in range(len(lista)):
        print(lista[i],end=" ")
    print()
        
#Função que recebe uma matri e o número de linhas e retorna a soma das linhas da matriz      
def Soma_Linhas(matriz,n):
    #declaracao do vetor que soma as linhas
    soma_linhas=[]
    #Para cada uma das linhas, calcula a sua soma
    for i in range(n):
        soma=0
        #Percorre as colunas da matriz
        for j in range(len(mat[i])):
            soma+=mat[i][j]
        #Adciona a soma a lista soma_linhas
        soma_linhas.append(soma)
    return soma_linhas

#Função que soma as coluna da matriz
def Soma_Colunas(mat,linhas,colunas):
    #declaracao do vetor que soma as colunas
    soma_colunas=[]
    #Percorre as colunas da matriz
    for j in range(colunas):
        #Incializa a soma das colunas
        soma=0
        for i in range(linhas):
            soma+=mat[i][j]
        soma_colunas.append(soma)
    #Devolve o vetor com a soma das colunas
    return soma_colunas     
        
#Função para calcular o maior elemento e devolver o índice
def Calcula_Maior(lista):
    #inicializa o maior elemento com o índice 0
    maior=0
    #Percorre a lista toda verificando se existe algum elemento maior elemento
    for i in range(len(lista)):
        #Se o maior elemento i for maior que o maior elemento
        #trocar o maior elemento
        if lista[i]>lista[maior]:
            maior=i
    #Devolve o indice do maior elemento
    return maior
    
#Função que recebe uma matriz, o número de linhas e devolve  a linha e a coluna que se encontra o menor elemento da matriz
def Calcula_Menor_Elemento(mat,linhas):
    #Inicializa a posição do menor elemento como 0.0
    menor_lin=0
    menor_colun=0
    
    #para cada um dos elementos da matriz
    for i in range(linhas):
        for j in range(len(mat[i])):
            #Se o elemento i,j for menor que o menor elemento, guardar a nova posição
            if mat[i][j]< mat[menor_lin][menor_colun]:
                menor_lin=i
                menor_colun=j
                
    #devolve a linha e a coluna do menor elemento
    return menor_lin, menor_colun

#Programa principal

#Leitura da dimensao da matriz
n,m=map(int,input().split())

#Leitura da matriz
mat=[]
Le_Matriz(mat,n)

#Calcula a soma das vendas de cada filial
vendas_filial=Soma_Linhas(mat,n)

#Calcula a soma das vendas em cada dia
vendas_dia=Soma_Colunas(mat,n,m)

#Calcula a filial que vedeu mais
maior_filial=Calcula_Maior(vendas_filial)

#Calcula o dia que mais vendeu
maior_dia=Calcula_Maior(vendas_dia)

#Calcula a filial e o dia que ocorreu a menor venda

menor_filial, menor_dia=Calcula_Menor_Elemento(mat,n)

#Impressão dos resultados

print("Vendas for Filial no Período: ")
Imprime_Lista(vendas_filial)


print("Vendas por dia no Período: ")
Imprime_Lista(vendas_dia)

print("Filial que mais vendeu no período ", maior_filial+1)

print("Dia que mais vendeu noPeríodo: ", maior_dia)

print("A menor venda de todas ocorreru na filial: ",menor_filial+1,"no dia: ",menor_dia+1, ".")




                  
    