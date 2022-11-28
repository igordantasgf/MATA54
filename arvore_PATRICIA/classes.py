#--------FORMATO DAS TRADUCOES NO ARQUIVO----------#   
#
# Arquivo final:
#     \  \ \ \_  4 bits: número de traduções = n
#      \  \ \__  2 bits: classe
#       \  \____ 30*7 bits: palavra origem 
#        \______ n*50*7 bits: traduções   
#
# Formato da lista a cada entrada: 
#
#--------------------------------------------------#
from ascii import *

class No():
    def __init__(self,lis,padrao,bit,pai,l,r,dir):
        self.lis = lis # caso não esteja vazio, contém endereço(s) das palavras no arquivo
        self.padrao = padrao   # padrao armazenado pelo nó de bifurcação
        self.bit = bit         # bit onde termina a análise do nó
        self.pai = pai
        self.l = None    
        self.r = None
        self.dir = None        # direção do nó, podendo ser 'l' ou 'r'

class Raiz():
    def __init__(self,raiz):
        self.raiz = raiz

    def inserir_no(self,file,lista): # lista de endereços das palavras no arquivo
        if self.raiz == None:                       
            self.raiz = No(lista,None,None,None,None,None,None)                   
        else:                                       
            self.inserir_no_n(file,lista,self.raiz,0)      

    def inserir_no_n(self,file,lista,no,bit):# 'no' indica o nó sendo lido,começando pela raiz    
        f = open(file, 'r+')                 # 'bit' indica em qual bit a analise de um padrao 
                                             #      na palavra deve começar

        if no.lis != None:  # caso o nó seja uma lista de endereços, 
                            #   uma bifurcação será criada
            
            f.seek(no.lis[0])
            palavra_no = f.read(MAX_PALAVRA)


            f.seek(lista[0])
            palavra = f.read(MAX_PALAVRA)
            
            padrao = ''
            
            # Compara as duas palavras até que ache uma dissonancia
            for i in range(int(bit),MAX_PALAVRA):  
                if palavra[i] != palavra_no[i]: 
                    break                       
                else:
                    padrao += palavra[i]

            no.bit = i-1 # no.bit indicando até qual bit as palvras são semelhantes
            no.padrao = padrao # armazena um padrão do bit 'bit' até o 'bit'+n

            # A palavra que possuir '0' na posição dissonante, vai para a esquerda, 
            #   e o outro para a direita

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
        
        if no.padrao != None: # caso o nó seja um padrão de caracteres

            f.seek(lista[0])   
            palavra = f.read(MAX_PALAVRA)

            # Primeiro, compara com o padrão do nó
            for i in range(bit,int(no.bit)):
                

                if palavra[i] != no.padrao[i-bit]: # se o padrão nao condiz com a palavra em algum indice i,
                    #   um novo nó será criando antes do nó em que o programa se encontra

                    # novo nó que ficará acima desse nó (nó antigo)
                    if bit==i:
                        novo_no = No(lis=None, padrao=no.padrao[0], bit=i, pai=no, l=None, r=None, dir=no.dir)
                    else:
                        novo_no = No(lis=None, padrao=no.padrao[bit:i], bit=i, pai=no, l=None, r=None, dir=no.dir)
                    
                    # assume um novo padrão para o nó antigo
                    no.padrao = no.padrao[i-no.bit:]

                    if no.pai!=None: ## coloca um novo filho para o pai do nó antigo, que é o novo nó
                        novo_no.pai = no.pai
                        if novo_no.padrao[0] == '0':
                            no.pai.l = novo_no
                        elif novo_no.padrao[0] == '1':
                            no.pai.r = novo_no
                        no.pai = novo_no

                    # a palavra será colocada a esquerda do novo nó se seu valor na dissonancia for 0,
                    #   e para a direita caso seja 1. No lado oposto, será colocado o nó antigo.
                    if palavra[i]=='0':
                        novo_no.l = No(lista, padrao=None, bit=None, pai=novo_no, l=None, r=None, dir='l')
                        no.dir = 'r'
                        novo_no.r = no
                        f.seek(novo_no.l.lis[0],0)
                    else:
                        novo_no.r = No(lista, padrao=None, bit=None, pai=novo_no, l=None, r=None, dir='r')
                        no.dir = 'l'
                        novo_no.l = no
                        f.seek(novo_no.r.lis[0],0)
                    f.close()
                    return

            # se o padrão condiz com a palavra, analisa o próximo bit fora do padrão
            #   para saber a direção em que se deve ir
            if palavra[no.bit+1]=='0': 
                self.inserir_no_n(file,lista,no.l,no.bit+1)
            elif palavra[no.bit+1]=='1':
                self.inserir_no_n(file,lista,no.r,no.bit+1)

    def lista_origem(self,raiz,endereços): # retorna os endereços presentes na raíz em pré-ordem
        if raiz.lis != None:
            endereços.append(raiz.lis[0])
            return
        if raiz.l != None:
            self.lista_origem(raiz.l,endereços)
        if raiz.r != None:
            self.lista_origem(raiz.r,endereços)
    
    def print_lista_origem(self,raiz,file,modo,boolbin): # modo: crescente ou decrescente
        endereços=[]                                     # boolbin: booleano para que a palavra 
        self.lista_origem(raiz,endereços)                #  esteja em binario ou nao
        palavras = []
        for i in endereços:
            f = open(file, 'r+')
            f.seek(i,0)
            palavras.append(binToWord(f.read(MAX_PALAVRA),'0'))
        if modo=='c':
            if boolbin==True:
                for i in sorted(palavras):
                    separadas = ''.join(i)
                    saida_sep = ''
                    for j in separadas:
                        saida_sep+= alfabeto.get(j)+' '
                    print(i, saida_sep)
            else:
                for i in sorted(palavras):
                    print(i)

        else:
            if boolbin==True:
                for i in reversed(sorted(palavras)):
                    separadas = i.split()
                    saida_sep = ''
                    for j in separadas:
                        saida_sep+= alfabeto.get(j)+' '
                    print(i, saida_sep)
            else:
                for i in sorted(palavras):
                    print(i)

    def lista_traducoes(self, file, palavra, no, bit):
        if no.bit != None:
            for i in range(bit, no.bit):
                if palavra[i] != no.padrao[i-bit]:
                    print('palavra inexistente no dicionario: {}'.format(binToWord(palavra, '0')))
                    return
            if palavra[no.bit]=='0':
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
            f.close()
            
    def consulta_classe(self, file, palavra, no, bit): 
        if no.lis==None and no.bit==None:
            print('palavra inexistente no dicionario: {}'.format(binToWord(palavra, '0')))
            return

        if no.bit != None:
            for i in range(bit, no.bit):
                if palavra[i] != no.padrao[i-bit]:
                    print('palavra inexistente no dicionario: {}'.format(binToWord(palavra, '0')))
                    return
            if palavra[no.bit+1]=='0':
                self.consulta_classe(file, palavra,no.l,no.bit+1)
            else:
                self.consulta_classe(file, palavra,no.r,no.bit+1)
            return
        if no.lis != None:
            f = open(file, 'r+')

            f.seek(no.lis[0])
            palavra = f.read(MAX_PALAVRA)

            f.seek(no.lis[0]-2)
            classe = binToClasse.get(f.read(2))
            print('classe da palavra: {} : {}'.format(binToWord(palavra,'0'),classe))
            f.close()
            return

    def lista_por_classe(self, file, classe, modo, no, bit):
        if no.lis==None and no.bit==None:
            return

        enderecos = []
        saida=[]
        self.lista_origem(no, enderecos)

        f = open(file,'r+')

        for i in enderecos:
            f.seek(i-2)
            c = binToClasse.get((f.read(2)))
            if c[0]==classe:
                saida.append(binToWord(f.read(MAX_PALAVRA),'0'))
        
        if modo=='c':
            for i in sorted(saida):
                print(i)
        else:
            for i in reversed(sorted(saida)):
                print(i)
        f.close()

    def imprimir_arvore(self, file, no):
        if no.bit != None:
            if no.l.bit != None: # analise esquerda
                x=no.l.bit+1
            else:
                f = open(file, 'r+')
                f.seek(no.l.lis[0])
                x = binToWord(f.read(MAX_PALAVRA),'0')
                f.close()
            if no.r.bit != None: # analise esquerda
                y=no.r.bit+1
            else:
                f = open(file, 'r+')
                f.seek(no.r.lis[0])
                y = binToWord(f.read(MAX_PALAVRA),'0')
                f.close()
            print('bit: {} fesq: {} fdir: {}'.format(no.bit+1,x,y))


            self.imprimir_arvore(file,no.l)
            self.imprimir_arvore(file,no.r)

        if no.lis != None:
            f = open(file, 'r+')
            f.seek(no.lis[0])
            print(binToWord(f.read(MAX_PALAVRA),'0'))
            f.close()
    
    def busca_palavra(self,file,palavra,no,bit,vari): # função auxiliar que permite dizer
        if no == None:                                #     se a palavra já está no dicionário
            return vari

        if no.bit != None:
            for i in range(bit, no.bit):
                if palavra[i] != no.padrao[i-bit]:
                    return vari
            if palavra[no.bit+1]=='0':
                vari=self.busca_palavra(file, palavra,no.l,no.bit+1,vari)
            else:
                vari=self.busca_palavra(file, palavra,no.r,no.bit+1,vari)
            return vari
        if no.lis != None:
            f = open(file,'r+')
            f.seek(no.lis[0])
            nobin = f.read(MAX_PALAVRA)
            if nobin==palavra:
                f.close()
                vari=0
                return vari
            else:
                f.close()
                return vari
