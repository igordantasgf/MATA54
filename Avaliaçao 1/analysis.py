"""Referências: 
https://medium.com/geekculture/performance-of-hash-implementations-on-various-workloads-fedac579a39b
https://medium.com/swlh/why-should-the-length-of-your-hash-table-be-a-prime-number-760ec65a75d1
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
from numpy import log as ln

path = "C:\\Users\igora\Documents\Material Faculdade\Estruturas de Dados e Algoritmos 2\MATA54\Avaliaçao 1\dados"
os.chdir(path)

# Leitura dos dados de acesso
def ler_arquivo(f):
    pacote = f.readlines()
    pacote = [int(x.replace('\n','')) for x in pacote]
    print(len(pacote))
    return pacote
    
f = ler_arquivo(open("dados_997.txt", 'r'))
g = ler_arquivo(open("dados_997_2027.txt", 'r'))

tam = f[0]
tam1 = g[0]

indices = list(range(1,tam+1))
def medias(a,b,indices,f):
    return [x/y for x,y in zip(f[a:b], indices)]

# Tabela com média de acessos com m de 1 até 997
tabela={'encad_explicito': medias(1, tam+1, indices, f),
        'hash_linear': medias(tam+1, 2*tam+1, indices, f) ,
        'hash_duplo': medias(2*tam+1, 3*tam+1, indices, f),
        'hash_quadratico': medias(3*tam+1, 4*tam+1, indices, f)}
df = pd.DataFrame(tabela)

#tabela com chaves com colisão
acessos = {}
acessos['encad_explicito'] = f[1:tam+1]
acessos['hash_linear'] = f[tam+1:2*tam+1]
acessos['hash_duplo'] = f[2*tam+1:3*tam+1]
acessos['hash_quadratico'] = f[3*tam+1:4*tam+1]
colisoes = {'encad_explicito': [],
            'hash_linear': [],
            'hash_duplo': [],
            'hash_quadratico': []}

# tabela com m extendido -> 4129
indices1 = list(range(1,tam1+1))
tabela1={'encad_explicito': medias(1, tam1+1, indices1, g),
        'hash_linear': medias(tam1+1, 2*tam1+1, indices1, g) ,
        'hash_duplo': medias(2*tam1+1, 3*tam1+1, indices1, g),
        'hash_quadratico': medias(3*tam1+1, 4*tam1+1, indices1, g)}
print('1.{}'.format(len(tabela1['encad_explicito'])))
print('2.{}'.format(len(tabela1['hash_linear'])))
print('3.{}'.format(len(tabela1['hash_duplo'])))
print('4.{}'.format(len(tabela1['hash_quadratico'])))
df1 = pd.DataFrame(tabela1)

# Chaves com colisão
for x in ['encad_explicito','hash_linear','hash_duplo','hash_quadratico']:
    count = 0
    val=0
    for i in range(len(df[x])):
        if acessos[x][i] != val+1:
            count+=1
        val=acessos[x][i]
        colisoes[x].append((count*100)/(i+1))

df_c = pd.DataFrame(colisoes)

#Leitura dos números aleatórios inseridos na tabela hash
g = open("numeros_inseridos.txt", 'r')
numeros = g.readlines()
numeros = [int(x.replace('\n','')) for x in numeros]
print(len(numeros))

#distribution frequency
dist = [i*0 for i in range(0,tam)]
numeros_part = numeros[0:5000]
for j in numeros_part:
    dist[j%tam] += 1
print('fim')

#Plotting
valores_x = np.linspace(0,1,tam)
valores_x1 = np.linspace(0,1,tam1)
x=np.linspace(0,1,200)
y=1/(1-x)
y2=1+(1/((1-x)**2))

#3 subplots - endereçamento aberto
fig, axs = plt.subplots(3, figsize=(15,7))
axs[0].plot(valores_x,df["hash_linear"], c='b')
axs[0].plot(valores_x1, df1["hash_linear"], c='b', linestyle='--')
axs[0].set_title('Hashing Linear')

axs[1].plot(valores_x,df["hash_duplo"], c='b')
axs[1].plot(valores_x1, df1["hash_duplo"], c='b', linestyle='--')
axs[1].set_title('Hashing Duplo')

axs[2].plot(valores_x,df["hash_quadratico"], c='b')
axs[2].plot(valores_x1, df1["hash_quadratico"], c='b', linestyle='--')
axs[2].set_title('Hashing Quadrático')

for val in [0,1,2]:
    axs[val].plot(x, y, c='g')
    axs[val].set_ylim((0,10))
    axs[val].set_ylabel("Média de acessos")
    axs[val].set_xlabel("Fator de carga")
    axs[val].legend(["Média de acessos - m=997",'Média de acessos - m=4129',"O(1/(1-α))"])


# media de todas as funções
fig, ax2 = plt.subplots(1, figsize=(15,5))
ax2.plot(valores_x,df['hash_linear'], c='r')
ax2.plot(valores_x,df['hash_duplo'], c='b')
ax2.plot(valores_x,df['hash_quadratico'], c='g')
ax2.plot(x, y, c='black', linestyle='--')
ax2.set_ylim((0,15))
ax2.set_title('Média de acessos para funções de endereçamento aberto')
ax2.set_ylabel("Média de acessos")
ax2.set_xlabel("Fator de carga")
ax2.legend(["Sondagem Linear","Hashing Duplo","Sondagem Quadrática","O(1/(1-α))"], loc='center')

# Chaves com colisão
fig, axs1 = plt.subplots(1, figsize=(15,5))
axs1.plot(list(np.linspace(0,100,len(valores_x))),df_c['encad_explicito'],c='orange')
axs1.plot(list(np.linspace(0,100,len(valores_x))),df_c['hash_linear'], c='r')
axs1.plot(list(np.linspace(0,100,len(valores_x))),df_c['hash_duplo'],c='b')
axs1.plot(list(np.linspace(0,100,len(valores_x))),df_c['hash_quadratico'],c='g')
axs1.legend(["Encadeamento Explícito","Sondagem Linear","Hashing Duplo","Sondagem Quadrática"], loc='center')
axs1.set_ylabel("Chaves com colisão (%)")
axs1.set_ylim(0,100)
axs1.set_xlabel("Total de chaves inseridas (%)")



y=1+x
valores_x2 = np.linspace(1,997,997)
fig, ax3 = plt.subplots(1, figsize=(15,5))
ax3.plot(valores_x,df['encad_explicito'], c='b')
ax3.plot(valores_x,df1['encad_explicito'], c='orange', linestyle='--')
ax3.plot(x,y, c='g')
ax3.set_ylim((0,5))
ax3.set_xticks([0,0.2,0.4,0.6,0.8,1.0],[0,200,400,600,800,1000])
ax3.set_title('Média de acessos - Encadeamento explícito')
ax3.set_ylabel("Média de acessos")
ax3.set_xlabel("Número de inserções")
ax3.legend(["Encadeamento explícito - m = 997","Encadeamento explícito - n = 997 - m = 2027","Θ(1-α)"], loc='center')

plt.show()

fig, ax = plt.subplots(1, 1, figsize=(15,5))
indices1 = list(range(0,tam))
ax.plot(numeros[0:tam])
ax.set_title("Distribuição dos valores inseridos na tabela", fontsize=14)
ax.set_xlabel("Números inseridos", fontsize=12)
ax.set_ylabel("Valor do número inserido", fontsize=12)


fig, ax1 = plt.subplots(1, 1, figsize=(15,5))
ax1.bar(indices1, dist)
ax1.set_title("Distribuição de restos da divisão pelo TABEL_SIZE", fontsize=14)
ax1.set_xlabel("Resto da divisão pelo TABLE_SIZE", fontsize=12)
ax1.set_ylabel("Número de ocorrências do valor 'x'", fontsize=12)

f.close()
g.close()