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
    def __init__(self,lis,l,r,bit):
        self.lis = lis # caso não esteja vazio, contém endereço(s) das palavras no arquivo
        self.bit = bit   # caso não esteja vazio, indica uma bifurcação, onde bit é a posição da palavra em que
        self.l = None    # a análise começa
        self.r = None

class Raiz():
    def __init__(self,raiz,tipo):
        self.raiz = raiz
        self.tipo = tipo    # Tipo = 0: arvore do idioma origem(palavra literal)
                            # Tipo = 1: arvore de traduçoes no idioma destino

    def inserir_no(self,file,lista,no):         # file
        if self.raiz == None:                       # lista: endereços no arquivo
            self.raiz = No(lista)                   # no: nó sendo analisado
        else:                                       # bit: bit onde a analise deve começar
            self.inserir_no_n(file,lista,no,2)      # começa pelo 2, pois os 2 primeiros indicam classe

    def inserir_no_n(self,file,lista,no,bit):    
        f = open(file, 'r+')

        if no.lis != None:  # caso o nó seja uma lista de endereços. 
            # Para o formato de árvore para palavras de origem,                                                            
            #   armazena-se o endereço dessa palavra e todas as
            #   suas traduções 
            

            if self.tipo == 0:  # idioma origem

                f.seek(no.lista[0]) 
                palavra_no = f.read(MAX_PALAVRA)

                f.seek(lista[0])
                palavra = f.read(MAX_PALAVRA)
            
                for i in range(bit,MAX_PALAVRA):    # 
                    if palavra[i] != palavra_no[i]: # comparação da palavra com a armazenada na árvore
                        break                       #

                no.bit = i  # bit diferenciável

                if palavra[i] == '0':
                    no.l = No(lista)
                    no.r = No(no.lis)
                    no.lis = None
                else:
                    no.l = No(no.lis)
                    no.r = No(lista)
                    no.lis = None
                f.close()
                return

            if self.tipo==1:
                # Para o formato de árvore de traduções, apenas
                #   uma palavra da lista é armazenada por nó.
                # A função será chamada para cada palavra obtida na main.

                f.seek(no.lista)    
                trad_no = f.read(MAX_TRADUCAO)

                f.seek(lista)
                trad_list = f.read(MAX_TRADUCAO)

                for i in range(bit, MAX_TRADUCAO):
                    if trad_list[i]!=trad_no[i]:
                        break
                no.bit = i

                if trad_no[i] == '0':
                    no.l = No(trad_no)
                    no.r = No(trad_list)
                    no.lis = None
                else:
                    no.l = No(trad_list)
                    no.r = No(trad_no)
                    no.lis = None
            f.close()
            return
        
        if no.bit != None:
            if self.tipo == 0:
                f.seek(lista[0])   
                palavra = f.read(MAX_PALAVRA)
                
                if palavra[no.bit] == '0':
                    if no.l != None:
                        self.inserir_no_n(file,lista,no.l,bit)
                    else:
                        no.l = No(lista)
                elif palavra[no.bit] == '1':
                    if no.r != None:
                        self.inserir_no_n(file,lista,no.r,bit)
                    else:
                        no.r = No(lista)
            if self.tipo == 1:
                f.seek(lista)
                trad = f.read(MAX_TRADUCAO)

                if trad[]
                # CONCLUIR
                    
    #def nova_raiz(self,file,lista,no,bit):    