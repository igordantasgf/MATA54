from arvore_PATRICIA.classes import *
from arvore_PATRICIA.ascii import *

file = 'idioma.dat'
root_origem = Raiz(None)  # definição da raíz da arvore PATRICIA
f = open(file,'w+')
f.close()
#----- Checa itens armazenados no arquivo e faz remake da arvore -----#
# A leitura é feita a partir do inicio do arquivo, considerando o formato
#   exposto nos comentários no arquivo 'classes.py'

f = open(file,'r+')
f.seek(0,2)
fim = f.tell()

if fim!=0:
    p=0                  # se não houver nada no arquivo, executa uma run
    f.seek(0,0)          # para os itens armazenados, e continua até chegar
    while f.tell()!=fim: # ao fim do arquivo
        n = bin_to_dec.get((f.read(4)))
        c = bin_classe.get((f.read(2)))

        endereços=[]
        endereços.append(f.tell())
        palavra = binToWord(f.read(MAX_PALAVRA),'0')
        for i in range(n):
            endereços.append(f.tell())
            f.read(MAX_TRADUCAO)
    
        valor=1                     # checa se a palavra já está na arvore, caso
        if root_origem.raiz!=None:  #   a arvore já possua algum item
            valor = (root_origem.busca_palavra(file,palavra,root_origem.raiz,0,valor))
        if valor==0:
            print("palavra ja existente: ",binToWord(palavra,'0'))
            continue
        
        root_origem.inserir_no(file, endereços) # caso não, insere na árvore
#---------------------------------------------------------------------#

while(True):
    val = input()

    if val == 'i': # inserir tradução

        palavra = transformToBin(input(),0)   
        t = input()      # classe da palavra
        n = int(input()) # número de traduções

        f = open(file, 'a+')
        endereços = []

        lista = []
        for i in range(n):
            lista.append(input())

        valor=1
        if root_origem.raiz!=None:
            valor = (root_origem.busca_palavra(file,palavra,root_origem.raiz,0,valor))
        if valor==0:
            print("palavra ja existente: ",binToWord(palavra,'0'))
            continue
        
        #------ Armazenamento das informações no arquivo ------#
        f.seek(0,2)
        f.write(decimais.get(n))
        f.write(classe.get(t))

        f.seek(0,2)
        endereços.append(f.tell())
        f.write(palavra)
        
        for i in lista:
            endereços.append(f.tell())
            f.write(transformToBin(i,1))
            f.seek(0,2)

        #------ inserção ------#
        root_origem.inserir_no(file, endereços)

        f.seek(endereços[0], 0)
        tamanho = MAX_PALAVRA
        saida = binToWord(f.read(tamanho),'0')
        print("palavra inserida no dicionario: {}".format(saida))
        print(transformToBin(saida, 0))

        # Caso o nó possua pai e é raíz, transforma pai em raíz
        if root_origem.raiz.pai != None:
            root_origem = root_origem.raiz.pai

        f.close()
    
    if val == 'l': # lista palavras no idioma origem
        root_origem.print_lista_origem(root_origem.raiz, file, input(), False)

    if val == 't': # traduções da palavra
        root_origem.lista_traducoes(file, transformToBin(input(),'0'), root_origem.raiz, 0)
    
    if val == 'a': # lista por classe
        root_origem.lista_por_classe(file,input(),input(),root_origem.raiz, bit=0)

    if val=='c': 
        root_origem.consulta_classe(file, transformToBin(input(),'0'), root_origem.raiz, 0)

    #if val=='r':

    if val=='p':
        root_origem.imprimir_arvore(file, root_origem.raiz)
        root_origem.print_lista_origem(root_origem.raiz, file, 'c', True)

    if val == 'e':
        exit(1)

    