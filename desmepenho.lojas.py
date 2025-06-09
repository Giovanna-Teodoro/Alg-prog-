#Entrada: a primeira linha da entrada contém dois inteiros n e m, representando,
#respectivamente o número de filiais e o número de meses de venda.
#Em seguida, são lidos n linhas contendo m inteiros cado.

#Saída: a saída é compopsta de 4 linhas.
#A primmeira linha contém as vendas totais de cada loja nos m meses do ano.
#A segunda linha, contém as vendas totais da rede em cada um dos meses.
#A terceira linha apresenta a loja que realizou a menor venda no período.
#A quarta linha contém o mês em que ocorreu a menor venda de todos e em qual loja
#isso ocorreu.


#entrada de n e m, filias e meses.


lojas, meses= map(int,input().split())


#declarar a matriz 
matriz=[]
matriz_meses_do_ano=["Janeiro","Fevereiro","Março","Abril", "Maio", "Junho"] 



#entrada dos dados da matriz
for i in range (lojas):
    matriz.append(list(map(int,input().split())))
  
  
  
#verificar a venda total de cada loja
desempenho_lojas=[]
soma=0


for i in range(lojas):
    for j in range(meses):
        soma+=matriz[i][j]
    desempenho_lojas.append(soma)
    print(desempenho_lojas[i], end=" ")
    soma=0
print()    
        
#verificar receita dos meses
receita_meses=[]
soma=0



for i in range(meses):
    for k in range(lojas):
        soma+=matriz[k][i]
    receita_meses.append(soma)
    print(receita_meses[i], end=" ")
    soma=0   
print()





#comparar qual a menor receita :
menor=0
for i in range(len(desempenho_lojas)):
    if desempenho_lojas[menor] > desempenho_lojas[i]:
        menor=i
print(f"Loja  {menor+1}")        






#varrer matriz e identificar a menor venda e por qual loja foi realizada.
menor_venda=0
mes_=0
for p in range(lojas):
    for q in range(meses):
        if matriz[menor_venda][mes_] > matriz[p][q]:
            menor_venda=p
            mes_=q
           
print(f"Mês de menor venda: {matriz_meses_do_ano[mes_]}. Loja: {menor_venda+1}.")        
            
            
        
    
