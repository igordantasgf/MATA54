def compressor_lzw(obj):
  alfabeto = sorted([i for i in set(''.join(obj))])

  # Criação de alfabeto inicial e dicionário
  var = 0
  dicionario = {}
  for i in alfabeto:
    dicionario[i] = var
    var+=1

  # Leitura do objeto (obj)
  cont,tam = 0,2 # começa-se com string de tamanho dois pois todas as letras do alfabeto já foram armazenadas
  while(True):
    if obj[cont : cont+tam] in dicionario.keys(): # Caso esteja no dicionário, incrementa o tamanho sendo analisado
      if cont+tam >= len(obj) :
        break
      tam+=1
      continue
    else: # Caso não esteja, coloca no dicionário e o novo índice iniciante é o último da palavra analisada anteriormente
      dicionario[obj[cont : cont+tam]] = str(var)
      var+=1
      cont = cont+tam-1
      tam=2
      continue

  return dicionario

def descompressor_lzw(obj, alfabeto):
  # Criação de alfabeto inicial e dicionário
  var = 0
  dicionario = {}
  for i in alfabeto:
    dicionario[i] = var
    var+=1

#print(compressor_lzw('010010101000010010101101111111010010101000010010101101111111010010101000010010101101111111010010101000010010101101111111010010101000010010101101111111010010101000010010101101111111'))


