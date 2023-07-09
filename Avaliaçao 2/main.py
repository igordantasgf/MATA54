from dict import dicionario_first
from algoritmos import *
from conversor import *


local_dict = None
while(True):
  local_dict = local_dict
  print('\n---------\n')
  i = input("\nDigite o comando:  ").split()

  # Comando para formar dicionario inicial, usado no descompressor (referenciado em algoritmos)
  # exemplo: make_dict aabaaacaade
  # return: {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5'}
  if i[0] == 'make_dict':
    local_dict = dicionario_first(i[1])
    print(local_dict)

  # Comando para comprimir um objeto
  # exemplo: compress aabaaacaade
  # return: objeto comprimido
  if i[0] == 'compress':

    # Para comprimir arquivos, citar o tipo
    # Ex: compress gif
    # colocar path do arquivo abaixo 
    if i[1] == 'gif':
      fig = 'nyan-cat'
      caminho_gif = f'C:/Users/igora/Documents/Material Faculdade/Estruturas de Dados e Algoritmos 2/MATA54/Avaliaçao 2/gif_files/{fig}.gif'
      compressor_lzw(''.join(convert_gif(caminho_gif)))
      continue

    if i[1] == 'mp3':
      caminho_mp3 = 'C:/Users/igora/Documents/Material Faculdade/Estruturas de Dados e Algoritmos 2/MATA54/Avaliaçao 2/mp3_files/oh-my-god-meme.mp3'
      compressor_lzw(convert_mp3(caminho_mp3))
      continue

    if i[1] == 'tiff':
      caminho_tiff = 'C:/Users/igora/Documents/Material Faculdade/Estruturas de Dados e Algoritmos 2/MATA54/Avaliaçao 2/tiff_files/2918043.tiff'
      compressor_lzw(convert_tiff(caminho_tiff))
      continue

    compressor_lzw(i[1:])

  # Comando para descomprimir um objeto, a partir de um dicionario
  #   inicial previamente feito
  # exemplo: decompress 1 1 2 6 1 3 6 4 5
  # return: objeto descomprimido
  if i[0] == 'decompress':
    #try:
    descompressor_lzw(i[1:], local_dict)
    #except TypeError:
      #print("Primeiro, gere um dicionario inicial com os caracteres usados através do comando make_dict")

  # Comando para encerrar a aplicação
  # end
  if i[0] == 'end':
    break

#adebcdebdcabecdbabebea
#adebcdebdcabecdbacdbea