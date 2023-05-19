"""Referências: 
https://medium.com/geekculture/performance-of-hash-implementations-on-various-workloads-fedac579a39b
https://medium.com/swlh/why-should-the-length-of-your-hash-table-be-a-prime-number-760ec65a75d1
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

path = "C:\\Users\igora\Documents\Material Faculdade\Estruturas de Dados e Algoritmos 2\MATA54\Avaliaçao 1"
os.chdir(path)

# Leitura dos dados de acesso
f = open("dados.txt", 'r')
pacote = f.readlines()
pacote = [int(x.replace('\n','')) for x in pacote]
print(len(pacote))

tam = pacote[0]

indices = list(range(1,tam+1))
def medias(a,b):
    return [x/y for x,y in zip(pacote[a:b], indices)]

# Tabela com média de acessos com m de 1 até 1001
tabela={'encad_explicito': medias(1, tam+1),
        'hash_linear': medias(tam+1, 2*tam+1) ,
        'hash_duplo': medias(2*tam+1, 3*tam+1),
        'hash_quadratico': medias(3*tam+1, 4*tam+1)}
df = pd.DataFrame(tabela)

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

fig, axs = plt.subplots(2, 2, figsize=(10,10))
axs[0][0].plot(valores_x,df['encad_explicito'])
axs[0][0].set_title("Encadeamento Explícito")
axs[0][0].set_xlabel("Fator de carga")
axs[0][0].set_ylabel("Média de acessos")
#axs[0][0].set_ylim((0,20))

axs[0][1].plot(valores_x,df['hash_linear'])
axs[0][1].set_title("Sondagem Linear")
axs[0][1].set_xlabel("Fator de carga")
axs[0][1].set_ylabel("Média de acessos")
#axs[0][1].set_ylim((0,20))

axs[1][0].plot(valores_x,df['hash_duplo'])
axs[1][0].set_title("Hashing Duplo")
axs[1][0].set_xlabel("Fator de carga")
axs[1][0].set_ylabel("Média de acessos")
#axs[1][0].set_ylim((0,20))

axs[1][1].plot(valores_x,df['hash_quadratico'])
axs[1][1].set_title("Sondagem Quadrática")
axs[1][1].set_xlabel("Fator de carga")
axs[1][1].set_ylabel("Média de acessos")
#axs[1][1].set_ylim((0,20))

fig, ax2 = plt.subplots(1, 1, figsize=(12,12))
ax2.plot(valores_x,df['encad_explicito'], c='r')
ax2.plot(valores_x,df['hash_linear'], c='g')
ax2.plot(valores_x,df['hash_duplo'], c='b')
ax2.plot(valores_x,df['hash_quadratico'], c='purple')
ax2.legend(['Encadeamento Explícito',"Sondagem Linear","Hashing Duplo","Sondagem Quadrática"], loc='center')
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