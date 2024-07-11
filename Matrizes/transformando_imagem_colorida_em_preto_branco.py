#importando bibliotecas de necessárias
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
#Lê uma Imagem e a converte em tons de cinza
img = Image.open('/workspaces/python-basico/Matrizes/assets/waldir azevedo criança com a flauta.jpg').convert('L')
img.save('waldir azevedo criança com a flauta preto e branco.png') # salva imagem em tons de cinza
# transforma informações da imagem em uma matriz numériaca
img_arr = np.array(img)
# gera imagem em tons de cinza na memória
plt.imshow(img_arr, cmap='gray', vmin=0, vmax=255)
#mostra imagem na tela
plt.show