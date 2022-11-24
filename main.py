from classes import *
from ascii import *

file = 'idioma.dat'
root_origem = Raiz(None)

while(True):
    val = input()

    if val == 'i': # inserir tradução
        
        t = input()      # classe da palavra
        n = int(input()) # número de traduções

        f = open(file, 'a+')
        endereços = []
        
        f.seek(0,2)
        f.write(decimais.get(n))
        f.write(classe.get(t))

        endereços.append(f.tell())
        palavra = transformToBin(input(),0,t)
        f.write(palavra)

        for i in range(n):
            traducao = transformToBin(input(),1,t)
            endereços.append(f.tell())
            f.write(traducao)
        print(endereços)

        root_origem.inserir_no(file, endereços)

        f.close()
    
