def dicionario_first(obj):
  var=1
  alfabeto = sorted([i for i in set(''.join(obj))])
  dicionario = {}
  for i in alfabeto:
    dicionario[i] = str(var)
    var+=1
  return dicionario