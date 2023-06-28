from dict import dicionario_first

def compressor_lzw(obj):
  print("\nPalavra a ser compressada: ",obj)

  # Criação de alfabeto inicial e dicionário
  dicionario = dicionario_first(obj)
  var = len(dicionario)
  saida=''

  # Leitura do objeto (obj)
  cont,tam = 0,2 # começa-se com string de tamanho dois pois todas as letras do alfabeto já foram armazenadas
 
  while(True):
    if obj[cont : cont+tam] in dicionario.keys(): # Caso esteja no dicionário, incrementa o tamanho sendo analisado
      if cont+tam >= len(obj) :
        saida = saida + str(dicionario[obj[cont : cont+tam-1]])
        break
      tam+=1
      continue
    else: # Caso não esteja, coloca no dicionário e o novo índice iniciante é o último da palavra analisada anteriormente
      dicionario[obj[cont : cont+tam]] = str(var)
      saida = saida + str(dicionario[obj[cont : cont+tam-1]])
      var+=1
      cont = cont+tam-1
      tam=2
      continue

  print("Resultado da compressão: ",saida)
  print("Dicionário da compressão: \n", dicionario)
  return dicionario


# O descompressor exite um "first_dict", dicionario previamente
# feito com todos os caracteres que estarão no obj a ser descompressado
def descompressor_lzw(obj, first_dict):
  print("\nPalavra a ser compressada: ",obj)

  # Criação de alfabeto inicial e dicionário
  dicionario = first_dict
  var=len(dicionario)
  cont = 0
  saida = ''

  # Loop, incrementando incondicionalmente os valores obj do dicionario ao feed
  # Analisa o feed, do inicio até quando encontrar um prefixo que não está no dicionario
  # Corta o feed do inicio até o penultimo item do prefixo adicionado ao dicionario
  while(True):
    if obj[cont] in dicionario.values():
      feed += [i for i in dicionario if i.values()==obj[cont]]

    tam = 1
    #for n in range(tam,len(feed)):
    #terminar...
    

  return 