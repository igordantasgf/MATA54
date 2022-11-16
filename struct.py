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

class No():
    def __init__(self,trad,l,r):
        self.trad = trad # endereço(s) da traducao no arquivo
        self.l = None
        self.r = None

class Raiz():
    def __init__(self,raiz):
        self.raiz = None

    def inserir_no(self,lista,file):     #   data: valor ou valores (em bin) a serem armazenados no arquivo
        if self.raiz == None:       #   destinos: endereco da palavra no arquivo 1 ou enderecos das traduções no arquivo 2
            self.raiz = No(lista)  
        else:
            self.inserir_no_n(lista) 

    def inserir_no_n(self,no,file):
        i

