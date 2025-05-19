#Faça  um programa que leia uma frase e conte quantas vogais existem na frase

frase=input().lower()

vogal="a,e,i,o,u,y"

contagem=0

for i in range(len(frase)):
    for j in range(len(vogal)):
        if frase[i] == vogal [j]:
            contagem+=1

print(contagem)