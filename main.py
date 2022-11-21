from classes import *
from ascii import *

file = 'idioma.dat'
root_origem = Raiz(None,0)
root_destino = Raiz(None,1)

while(True):
    val = input()

    if val == 'i': # inserir tradução
        
        c = input()      # classe da palavra
        n = int(input()) # número de traduções

        f = open(file, 'a+')
        endereços = []
        
        palavra = transformToBin(input(),0,c)
        f.seek(0,2)
        f.write(decimais.get(n))
        endereços.append(f.tell())
        f.write(palavra)

        for i in range(n):
            traducao = transformToBin(input(),0,c)
            endereços.append(f.tell())
            f.write(traducao)
            # CONCLUIR