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

            #print('Aqui há uma lista e a origem é:', binToWord(palavra_no,'0'))

            f.seek(lista[0])
            palavra = f.read(MAX_PALAVRA)
            
            padrao = ''
            for i in range(int(bit),MAX_PALAVRA):    # 
                if palavra[i] != palavra_no[i]: # comparação da palavra com a armazenada na árvore
                    break                       #
                else:
                    padrao += palavra[i]

            no.bit = i-1
            #no.padrao = palavra[bit:i-1] # padrão desse no
            no.padrao = padrao

            if palavra[i] == '0':
                #print('{} inserido na esquerda'.format(binToWord(palavra,'0')))
                #print('{} inserido na direita'.format(binToWord(palavra_no,'0')))
                no.l = No(lis=lista, padrao=None, bit=None, pai=no, l=None, r=None, dir='l')
                no.r = No(lis=no.lis, padrao=None, bit=None, pai=no, l=None, r=None, dir='r')
                no.lis = None

            else:
                #print('{} inserido na direita'.format(binToWord(palavra,'0')))
                #print('{} inserido na esquerda'.format(binToWord(palavra_no,'0')))
                no.l = No(lis=no.lis, padrao=None, bit=None, pai=no, l=None, r=None, dir='l')
                no.r = No(lis=lista, padrao=None, bit=None, pai=no, l=None, r=None, dir='r')
                no.lis = None

            f.close()
            return
        
        if no.padrao != None: # caso o nó seja um padrão de caracteres

            f.seek(lista[0])   
            palavra = f.read(MAX_PALAVRA)

            #print("Aqui há um padrão até o bit {} e o padrao até aqui é {}".format(no.bit,no.padrao))
            
            # Primeiro, compara com o padrão do nó
            #print('primeiro: ',bit+1)
            #print('segundo: ',int(no.bit)+1)
            #print('palavra[i]: ',palavra)
            #print('no.padrao[i]: ',no.padrao)
            for i in range(bit,int(no.bit)+1):
                #print('valor de i: ',i)
                if palavra[i] != no.padrao[i-no.bit]: # se o padrão nao condiz com a palavra em algum indice i

                    #print('inserindo a palavra {} antes do nó'.format(binToWord(palavra,'0')))
                    # novo nó que ficará acima desse nó
                    if bit==i:
                        novo_no = No(lis=None, padrao=no.padrao[0], bit=i, pai=no, l=None, r=None, dir=no.dir)
                    else:
                        novo_no = No(lis=None, padrao=no.padrao[bit:i], bit=i, pai=no, l=None, r=None, dir=no.dir)
                    #print('novo no com padrao', novo_no.padrao, ' e bit ',novo_no.bit)

                    no.padrao = no.padrao[i-no.bit:]
                    no.bit = i

                    if no.pai!=None: ## coloca um novo filho para o nó pai
                        novo_no.pai = no.pai
                        if novo_no.padrao[0] == '0':
                            #print("Padrao do no pai : ",no.pai.padrao,'. novo_no a esquerda desse no')
                            no.pai.l = novo_no
                        elif novo_no.padrao[0] == '1':
                            #print("Padrao do no pai : ",no.pai.padrao,'. novo_no a direira desse no')
                            no.pai.r = novo_no
                        no.pai = novo_no

                    if palavra[i]=='0':
                        novo_no.l = No(lista, padrao=None, bit=None, pai=novo_no, l=None, r=None, dir='l')
                        no.dir = 'r'
                        novo_no.r = no
                        f.seek(novo_no.l.lis[0],0)
                        #print('esq: {}'.format(binToWord(f.read(MAX_PALAVRA),'0')))
                        #print('dir: padrão ',no.padrao)
                    else:
                        novo_no.r = No(lista, padrao=None, bit=None, pai=novo_no, l=None, r=None, dir='r')
                        no.dir = 'l'
                        novo_no.l = no
                        #print('esq: padrão ',no.padrao)
                        f.seek(novo_no.r.lis[0],0)
                        #print('dir: {}'.format(binToWord(f.read(MAX_PALAVRA),'0'))) 
                    return

            # se o padrão condiz com a palavra
            j=i
            if palavra[no.bit+1]=='0': # i+1 já vai estar fora do padrão analisado no nó
                #print('INDO para a esquerda')
                self.inserir_no_n(file,lista,no.l,j+1)
            elif palavra[no.bit+1]=='1':
                #print('INDO para a direita')
                self.inserir_no_n(file,lista,no.r,j+1)

    def lista_origem(self,raiz,endereços):
        if raiz.lis != None:
            endereços.append(raiz.lis[0])
            #print(raiz.lis[0])
            return
        if raiz.l != None:
            #print('tem algo na esquerda')
            #if raiz.l.padrao!=None:
                #print(raiz.l.padrao)
            #if raiz.l.lis != None:
                #print('tem palavra:')
            self.lista_origem(raiz.l,endereços)
        if raiz.r != None:
            #print('tem algo na direita')
            #if raiz.r.padrao!=None:
                #print(raiz.r.padrao)
            #if raiz.r.lis != None:
                #print('tem palavra:')
            self.lista_origem(raiz.r,endereços)
    
    def print_lista_origem(self,raiz,file,modo):
        endereços=[]
        self.lista_origem(raiz,endereços)
        #print(endereços)
        palavras = []
        for i in endereços:
            f = open(file, 'r+')
            f.seek(i,0)
            #print(f.read(MAX_PALAVRA))
            palavras.append(binToWord(f.read(MAX_PALAVRA),'0'))
        if modo=='c':
            for i in sorted(palavras):
                print(i)
        else:
            for i in reversed(sorted(palavras)):
                print(i)

    def lista_traducoes(self, file, palavra, no, bit):
        if no.bit != None:
            for i in range(bit, no.bit+1):
                if palavra[i] != no.padrao[i-bit]:
                    print('palavra inexistente no dicionario: {}'.format(binToWord(palavra, '0')))
                    return
            if palavra[no.bit+1]=='0':
                self.lista_traducoes(file, palavra,no.l,no.bit+1)
            else:
                self.lista_traducoes(file, palavra,no.r,no.bit+1)
            return
        if no.lis != None:
            f = open(file, 'r+')

            f.seek(no.lis[0])
            print('traducoes da palavra: {}'.format(binToWord(f.read(MAX_PALAVRA),'0')))

            traducoes=[]
            for i in no.lis[1:]:
                f.seek(i)
                traducoes.append(f.read(MAX_TRADUCAO))
            for i in traducoes:
                print(binToWord(i, '1'))
              
