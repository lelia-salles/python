import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Lê uma Imagem e a converte em tons de cinza
img = Image.open('/workspaces/python-basico/Matrizes/assets/waldir azevedo criança com a flauta.jpg').convert('L')
img.save('waldir azevedo criança com a flauta preto e branco.png')  # salva imagem em tons de cinza

# Transforma informações da imagem em uma matriz numérica
img_arr = np.array(img)

# Imprime a forma da matriz da imagem
print("Shape da matriz da imagem:", img_arr.shape)

# Gera imagem em tons de cinza na memória
plt.imshow(img_arr, cmap='gray', vmin=0, vmax=255)

# Mostra imagem na tela
plt.show()  # Adicione esta linha para exibir a imagem
