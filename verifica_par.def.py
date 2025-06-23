def verifica_par(num):
    if num%2==0:
        return True
    else:
        return False
    

num=int(input())

par=verifica_par(num)
print(par)