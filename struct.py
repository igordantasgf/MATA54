#--------FORMATO DAS TRADUCOES NO ARQUIVO----------#   
# 
# Arquivo 1: árvore para idioma origem
#      | |   Modelo:
#      | L-> 2 bytes: classe da palavra
#      L---> 30 bytes: todos os bits da palavra
#    
#    
#
# Arquivo 2: árvore para traduções
#      | |   Modelo:
#      | L-> 2 bytes : classe da palavra
#      L---> 50 bytes: todos os bits da palavra         
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
        self.raiz = None
        self.tipo = tipo    # Tipo = 0: arvore do idioma origem(palavra literal)
                            # Tipo = 1: arvore de traduçoes no idioma destino

    def inserir_no(self,file,lista,no,bit):         # file
        if self.raiz == None:                       # lista: endereços no arquivo
            self.raiz = No(lista)                   # no: nó sendo analisado
        else:                                       # bit: bit onde a analise deve começar
            self.inserir_no_n(file,lista,no,0) 

    def inserir_no_n(self,file,lista,no,bit):    
        #analisando 

        if no.lista != None:

            f = open(file,'r+')                     # primeiro endereço é da palavra original
            f.seek(no.lis[0])                     
            palavra_no = f.read(MAX_PALAVRA)

            if self.tipo == 0:                          # idioma origem
                #f = open(file,'r+')                     # primeiro endereço é da palavra original
                #f.seek(no.lista[0])                     
                #palavra_no = f.read(MAX_PALAVRA)
                palavra = lista[0]
            
                for i in range(bit,MAX_PALAVRA):
                    if palavra[i] != palavra_no[i]:
                        break

                no.bit = i

                if palavra[i] == '0':
                    no.l = No(lista)
                    no.r = No(no.lis)
                    no.lis = None
                else:
                    no.l = No(no.lis)
                    no.r = No(lista)
                    no.lis = None