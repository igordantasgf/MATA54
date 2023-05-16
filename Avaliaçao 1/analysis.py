import matplotlib.pyplot as plt
import pandas as pd
import os

path = "C:\\Users\igora\Documents\Material Faculdade\Estruturas de Dados e Algoritmos 2\MATA54\Avaliaçao 1\output"
os.chdir(path)

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

fig, axs = plt.subplots(2, 2, figsize=(5,5))
axs[0][0].plot(df['encad_explicito'])
axs[0][1].plot(df['hash_linear'])
axs[1][0].plot(df['hash_duplo'])
axs[1][1].plot(df['hash_quadratico'])
plt.show()

f.close()