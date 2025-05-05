#Querendo saber se um dado é viciado, Josemar anotou quantas vezes cada face de um dado saiu. Faça um programa que leia a face soteada de um dado lançado n vezes, 
# #até que o usuário digite -1. Em seguida, seu programa deve imprimir quantas vezes cada face saiu.
# Entrada 1 , 2 , 6, 5, 2, 3, 5, 4, 1, 6, 5, 2, 3, -1
#Saída : 2 3 2 1 3 2


#Leiura das faces

faces=[0]*6
num= int(input()) # entrada da primeira jogada 

while num != -1: # condição de verificação para continuar jogando ou interromper o programa 5
    faces[num-1]= faces[num-1]+1
    num= int(input()) # entrada  das próximas jogadas
for i in range(6):  #laço de impressão da qnt de vezes jogada cada número com i percorrendo a lista 
    print(faces[i], end=" ")    