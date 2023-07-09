from PIL import Image
import binascii

def convert_gif(path):
  # Open the GIF file
  image = Image.open(path)

  # Convert the image to RGB mode (if needed)
  image = image.convert('RGB')

  # Get the pixel data as a sequence of RGB tuples
  pixels = image.getdata()

  # Convert each RGB tuple to a hexadecimal value
  hex_values = [f'#{r:02x}{g:02x}{b:02x}' for r, g, b in pixels]

  # Print the hexadecimal values
  return hex_values

def convert_mp3(path):
  with open(path, 'rb') as file:
    mp3_data = file.read()

  hex_data = mp3_data.hex()
  return hex_data

# Exemplo de uso
#mp3_file_path = 'C:/Users/igora/Documents/Material Faculdade/Estruturas de Dados e Algoritmos 2/MATA54/Avaliaçao 2/oh-my-god-meme.mp3'
#print(convert_mp3(mp3_file_path))

def convert_tiff(file_path):
  with open(file_path, 'rb') as file:
    tiff_data = file.read()

  hex_data = tiff_data.hex()
  return hex_data

#print(convert_tiff('C:/Users/igora/Documents/Material Faculdade/Estruturas de Dados e Algoritmos 2/MATA54/Avaliaçao 2/tiff_files/2918043.tiff'))