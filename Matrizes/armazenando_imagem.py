# importação da biblioteca
from matplotlib.image import imread
# leitura da imagm com a função imread()
imagem = imread('/workspaces/python-basico/Matrizes/assets/waldir azevedo criança com a flauta.jpg')
# exibição da imagem
print("altura em pixels: ", end= " ")
print(imagem.shape[0]) # altura da imagem
print("largura em pixels: ", end= " ")
print(imagem.shape[1])
print("canais de cor: ", imagem.shape[2]) # outra forma de escrever

