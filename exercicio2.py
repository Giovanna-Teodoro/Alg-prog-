#Faça um programa que leia um inteiro n e, em seguida leia n linhas contendo um inteiro cada.
# Por fim, calcule a soma dos elementos de índice par e a media dos elementos de índice ímpar.

#leitura de um n linhas

nu= int(input())
par=0
impar=0
i=0
total_imp=0
vet=[]
while i < nu:
    entrada=int(input())
    vet.append(entrada)
    i+=1 
for n in range (len(vet)):
    if n%2==0:
        par= par + vet[n]
    else:
        impar= impar+ vet[n]
        total_imp+=1
      
media_imp= impar / total_imp

print(par,"\n",media_imp )

