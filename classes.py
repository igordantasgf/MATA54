#--------FORMATO DAS TRADUCOES NO ARQUIVO----------#   
#
# Arquivo final:
#     \  \   \_ 4 bits: número de traduções = n
#      \  \  
#       \  \____ (2+30*7) bits: classe+palavra origem 
#        \______ n*(2+50*7) bits: classe+traduções   
#
# Formato da lista a cada entrada: 
#
#--------------------------------------------------#
from ascii import *

class No():
    def __init__(self,lis,padrao,bit,pai,l,r,dir):
        self.lis = lis # caso não esteja vazio, contém endereço(s) das palavras no arquivo
        self.padrao = padrao   # caso não esteja vazio, indica uma bifurcação, com o mesmo padrão
        self.bit = bit  # bit onde termina a análise do nó
        self.pai = pai
        self.l = None    # a análise começa
        self.r = None
        self.dir = None

class Raiz():
    def __init__(self,raiz):
        self.raiz = raiz

    def inserir_no(self,file,lista):         # file
        if self.raiz == None:                       # lista: endereços no arquivo
            self.raiz = No(lista,None,None,None,None,None,None)                   # no: nó sendo analisado
        else:                                       # bit: bit onde a analise deve começar
            self.inserir_no_n(file,lista,self.raiz,0)      # começa pelo 2, pois os 2 primeiros indicam classe

    def inserir_no_n(self,file,lista,no,bit):    
        f = open(file, 'r+')

        if no.lis != None:  # caso o nó seja uma lista de endereços. 
            # Para o formato de árvore para palavras de origem,                                                            
            #   armazena-se o endereço dessa palavra e todas as
            #   suas traduções 

            f.seek(no.lis[0])
            palavra_no = f.read(MAX_PALAVRA)

            f.seek(lista[0])
            palavra = f.read(MAX_PALAVRA)
            
            padrao = ''
            for i in range(int(bit),MAX_PALAVRA):    # 
                if palavra[i] != palavra_no[i]: # comparação da palavra com a armazenada na árvore
                    break                       #
                else:
                    padrao += palavra[i]

            no.bit = i
            no.padrao = palavra[bit:i-1] # padrão desse no

            if palavra[i] == '0':
                no.l = No(lis=lista, padrao=None, bit=None, pai=no, l=None, r=None, dir='l')
                no.r = No(lis=no.lis, padrao=None, bit=None, pai=no, l=None, r=None, dir='r')
                no.lis = None
            else:
                no.l = No(lis=no.lis, padrao=None, bit=None, pai=no, l=None, r=None, dir='l')
                no.r = No(lis=lista, padrao=None, bit=None, pai=no, l=None, r=None, dir='r')
                no.lis = None
            f.close()
            return
        
        if no.padrao != None:

            f.seek(lista[0])   
            palavra = f.read(MAX_PALAVRA)
            
            # Primeiro, compara com o padrão do nó
            for i in range(int(no.bit), int(no.bit)+len(no.padrao)):
                print('primeiro: ',int(no.bit))
                print('segundo: ',len(no.padrao))
                if palavra[i] != no.padrao[i]: # se o padrão nao condiz com a palavra em algum indice i

                    novo_no = No(lis=lista, padrao=None, bit=no.bit, pai=no, l=None, r=None, dir=no.dir)
                    novo_no.padrao = no.padrao[no.bit:i-1]
                    
                    no.padrao = no.padrao[i:no.bit+len(no.padrao)]
                    no.bit = i
                    if no.pai!=None:
                        no.pai = novo_no
                        if no.dir == 'l':
                            no.pai.l = novo_no
                        else:
                            no.pai.r = novo_no
                    
                    if palavra[i]=='0':
                        novo_no.l = No(lista, padrao=None, bit=None, pai=novo_no, l=None, r=None, dir='l')
                        no.dir = 'r'
                        novo_no.r = no
                    else:
                        novo_no.r = No(lista, padrao=None, bit=None, pai=novo_no, l=None, r=None, dir='r')
                        no.dir = 'l'
                        novo_no.l = no
                    break

                else: # se o padrão condiz com a palavra

                    if palavra[i+1]=='0': # i+1 já vai estar fora do padrão analisado no nó
                        self.inserir_no_n(file,lista,no.l,i+1,'l')
                    elif palavra[i+1]=='1':
                        self.inserir_no_n(file,lista,no.r,i+1,'r')
                    break

    def lista_origem(self,raiz,endereços):
        if raiz.l != None:
            self.lista_origem(raiz.l,endereços)
        else:
            if raiz.r != None:
                self.lista_origem(raiz.r,endereços)
            else:
                endereços.append(raiz.lis[0])
    
    def print_lista_origem(self,raiz,file):
        endereços=[]
        self.lista_origem(raiz,endereços)
        print(endereços)
        palavras = []
        for i in endereços:
            f = open(file, 'r+')
            f.seek(i,0)
            print(f.read(MAX_PALAVRA))
            palavras.append(binToWord(f.read(MAX_PALAVRA),'0'))
        print(sorted(palavras))
