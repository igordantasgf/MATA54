from classes import *
from ascii import *

file = 'idioma.dat'
root_origem = Raiz(None)

while(True):
    val = input()

    if val == 'i': # inserir tradução


        palavra = transformToBin(input(),0)
        t = input()      # classe da palavra
        n = int(input()) # número de traduções

        f = open(file, 'a+')
        endereços = []
        
        f.seek(0,2)
        f.write(decimais.get(n))
        f.write(classe.get(t))

        endereços.append(f.tell())
        f.write(palavra)

        for i in range(n):
            traducao = transformToBin(input(),1)
            endereços.append(f.tell())
            f.write(traducao)

        root_origem.inserir_no(file, endereços)

        f.seek(endereços[0], 0)
        tamanho = MAX_PALAVRA
        saida = binToWord(f.read(tamanho),'0')
        print("palavra inserida no dicionario: {}".format(saida))

        #buscando novo root
        if root_origem.raiz.pai != None:
            root_origem = root_origem.raiz.pai

        f.close()
    
    if val == 'l': # lista palavras no idioma origem
        root_origem.print_lista_origem(root_origem.raiz, file)
