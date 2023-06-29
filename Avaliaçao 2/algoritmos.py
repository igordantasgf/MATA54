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





# O descompressor exite um dicionario previamente
# feito com todos os caracteres que estarão no obj a ser descompressado
def descompressor_lzw(obj, dicionario):
  print("\nPalavra a ser descompressada: ",obj)

  # Criação de alfabeto inicial e dicionário
  var=len(dicionario)
  cont = 0
  saida = ''
  feed = ''

  # Loop, incrementando incondicionalmente os valores obj do dicionario ao feed
  # Analisa o feed, do inicio até quando encontrar um prefixo que não está no dicionario
  # Corta o feed do inicio até o penultimo item do prefixo adicionado ao dicionario
  while(True):
    if cont==len(obj):
      break

    if obj[cont] in dicionario.values():
      #print('i = ',[i for i in dicionario if dicionario[i]==obj[cont]][0])
      saida += [i for i in dicionario if dicionario[i]==obj[cont]][0]
      feed += [i for i in dicionario if dicionario[i]==obj[cont]][0]
      cont+=1
      #print('Saida:',saida)

    while(True):
      mudou = False
      if len(feed)>1 and feed not in dicionario:
        #print("Condição 1")
        for i in range(2,len(feed)+1):
          if feed[0:i] not in dicionario:
            #print("Condição 2\nFeed atual:",feed)
            dicionario[feed[0:i]] = str(var)
            var+=1
            feed = feed[i-1:]
            mudou = True
            #print("Novo feed:",feed)
            break
      if mudou==True:
        continue
      else:
        break
  
  print("Resultado da descompressão:",saida)
  print("Dicionário da descompressão: \n", dicionario)