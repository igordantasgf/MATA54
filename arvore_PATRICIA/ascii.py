'''
alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
ascii = {}
j=0
for i in range(97, 123):
    ascii[alfabeto[j]]=i
    j+=1
'''
alfabeto={' ':'0100000','a':'1100001','b':'1100010','c':'1100011','d':'1100100','e':'1100101','f':'1100110','g':'1100111','h':'1101000','i':'1101001','j':'1101010','k':'1101011','l':'1101100','m':'1101101','n':'1101110','o':'1101111','p':'1110000','q':'1110001','r':'1110010','s':'1110011','t':'1110100','u':'1110101','v':'1110110','w':'1110111','x':'1111000','y':'1111001','z':'1111010'}
bin_to_l={'0100000':' ','1100001':'a','1100010':'b','1100011':'c','1100100':'d','1100101':'e','1100110':'f','1100111':'g','1101000':'h','1101001':'i','1101010':'j','1101011':'k','1101100':'l','1101101':'m','1101110':'n','1101111':'o','1110000':'p','1110001':'q','1110010':'r','1110011':'s','1110100':'t','1110101':'u','1110110':'v','1110111':'w','1111000':'x','1111001':'y','1111010':'z'}
classe = {'s': '00','a':'01','v':'10'}
bin_classe = {'00':'s','01':'a','10':'v'}
binToClasse = {'00': 'substantivo','01':'adjetivo','10':'verbo'}
decimais = {1:'0001',2:'0010', 3:'0011',4:'0100',5:'0101',6:'0110',7:'0111',8:'1000',9:'1001',10:'1010'}
bin_to_dec = {'0001':1,'0010':2, '0011':3,'0100':4,'0101':5,'0110':6,'0111':7,'1000':8,'1001':9,'1010':10}
MAX_PALAVRA = 7*30
MAX_TRADUCAO = 7*50

def transformToBin(word,tipo): # t = tipo (origem ou traducoes)
    word = ''.join(word)      
    saida = ''                  

    for i in word:
        saida+=alfabeto.get(i)

    if tipo==0 and len(saida)<MAX_PALAVRA:
        saida+='0'*(MAX_PALAVRA-len(saida))

    if tipo==1 and len(saida)<MAX_TRADUCAO:
        saida+='0'*(MAX_TRADUCAO-len(saida))

    return saida

def binToWord(binario, tipo):
    binario.split(' ')
    palavra=''
    saida=''
    if tipo=='0':
        for k in range(0,MAX_PALAVRA):
            palavra+=binario[k]
            if (k+1)%7==0:
                if palavra=='0000000':
                    break
                saida+=bin_to_l.get(palavra)
                palavra=''
    else:
        for k in range(0,MAX_TRADUCAO):
            palavra+=binario[k]
            if (k+1)%7==0:
                if palavra=='0000000':
                    break
                saida+=bin_to_l.get(palavra)
                palavra=''
    return saida