#area 
def calcula_area(x,y):
    area=x*y
    return(area)

#perimetro

def calcula_perime(a,b):
    perimetro=(a*2)+(b*2)
    return (perimetro)

base,altura=map(float,input().split())

area=calcula_area(base,altura)
perimetro= calcula_perime(base,altura)
print(area, perimetro)

