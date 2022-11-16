'''
alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
ascii = {}
j=0
for i in range(97, 123):
    ascii[alfabeto[j]]=i
    j+=1
'''
hex_ascii = {' ': 32, 'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122}
tipo = {'s':0b00,'a':0b01,'v':0b10}

def MAX_PALAVRA(): return 7*30
def MAX_TRADUCAO(): return 7*50

def transformToBin(word,tipo):  # tipo:
    word = ''.join(word)        #   0: idioma origem 
    saida = ''                  #   1: dicionario (traduções)

    for i in word:
        saida+=bin(hex_ascii.get(i))[2:]

    if tipo==0 and len(saida)<MAX_PALAVRA():
        saida+='0'*(MAX_PALAVRA()-len(saida))

    if tipo==1 and len(saida)<MAX_TRADUCAO():
        saida+='0'*(MAX_TRADUCAO()-len(saida))

    return saida