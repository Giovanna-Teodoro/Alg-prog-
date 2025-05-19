
#Faça um programa que leia  o número d elinhas e colunas de uma matriz . EM seguida seu programa deve ler os elmentos da matriz. Por fim, calcule a soma das linhas e das colunas da matriz. 
#ENTRADA                           
# 4 3                 # Soma da linha 1:8         # soma da coluna  2:23
# 1 4 3               # soma da linha 2:11        # soma da coluna   3:30
# 2 0 9               # soma da linha 3:11
# 3 7 10              # soma da linha  4:21
# 1 12 8              # soma da coluna  1:7  



#Faça um programa que leia a dimensão d euma matriz quadrada nxm. EM seguida, leia os elementos da matriz. Por fim, calcule a soma da diagonal principal e da diagonal secundária.
#Ex
# 3                         Soma da diagonal principal : 13
# 1 4 3                     #Somda da diagonal secundária : 6 
# 2 3 7
# 0 5 9



#Leitura do número de linhas da matriz
i
line, raw = map(int,input().split())

matriz= []

for i in range(line):
    linhas= []
    linhas= list(map(int, input().split()))
    matriz.append(linhas)

soma=[]*line    
for i in range (line):
    calcl=0
    for n in  range(raw):
         calcl= calcl + matriz[i][n]
    soma.append(calcl)
    print(f"A soma da linha {linhas[i]}:",soma[i])

reslt=[]*raw
for i in range(raw):
    calcl=0
    for n in range (line):
        calcl += matriz[n][i]
    reslt.append(calcl)
    print(f"A soma da coluna {i}:", reslt[i])    





line, raw = map(int,input().split())

matriz= []

for i in range(line):
    linhas= []
    linhas= list(map(int, input().split()))
    matriz.append(linhas)

soma=[]*line    
for i in range (line):
#    calcl=0
    for n in  range(raw):
         soma[i]+=matriz[i][n]
    print(f"A soma da linha {i}:",soma[i])

reslt=[]*raw
for i in range(raw):
#    calcl=0
    for n in range (line):
        reslt[i]+=matriz[i][n]
#    reslt.append(calcl)
    print(f"A soma da coluna {i}:", reslt[i])    

