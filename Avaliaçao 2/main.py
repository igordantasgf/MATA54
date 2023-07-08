from dict import dicionario_first
from algoritmos import *


local_dict = None
while(True):
  local_dict = local_dict
  print('\n---------\n')
  i = input("\nDigite o comando:  ").split()

  # Comando para formar dicionario inicial, usado no descompressor (referenciado em algoritmos)
  # exemplo: make_dict aabaaacaade
  # return: {'a': '0', 'b': '1', 'c': '2', 'd': '3', 'e': '4'}
  if i[0] == 'make_dict':
    local_dict = dicionario_first(i[1])
    print(local_dict)

  # Comando para comprimir um objeto
  # exemplo: compress aabaaacaade
  # return: objeto comprimido
  if i[0] == 'compress':
    compressor_lzw(i[1])

  # Comando para descomprimir um objeto, a partir de um dicionario
  #   inicial previamente feito
  # exemplo: decompress 0 0 1 5 0 2 5 3 4
  # return: objeto descomprimido
  if i[0] == 'decompress':
    #try:
    descompressor_lzw(i[1], local_dict)
    #except TypeError:
      #print("Primeiro, gere um dicionario inicial com os caracteres usados através do comando make_dict")

  # Comando para encerrar a aplicação
  # end
  if i[0] == 'end':
    break

#adebcdebdcabecdbabebea
#adebcdebdcabecdbacdbea