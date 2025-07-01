#Função que recebe dois números e devolve em ordem crescente
def Ordena_Num(n1,n2):
    #Se o n1 for menor ou igual a n2, devolve na ordem n1, n2
    if n1<=n2:
        return n1, n2
    else:
        return n2, n1



#Programa principal
n1, n2= map(int, input().split())

#Ordena os dois números em ordem crescente

n1, n2= Ordena_Num(n1,n2)

#Impressão em ordem crescente

print(n1, n2)