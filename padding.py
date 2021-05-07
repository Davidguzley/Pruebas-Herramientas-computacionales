#Libreria numpy para matrices.
import numpy as np

def padding(image, padded_size):
    """Aplica padding a una matriz
    """
    image_row, image_col = image.shape #Asigna alto y ancho de la imagen.

    padded_image = np.zeros((image_row + padded_size*2, image_col + padded_size*2)) #Matriz de imagen con padding en zeros.
    print("Padded image zeros:")
    print(padded_image)

    padded_image[padded_size:padded_size + image_row, padded_size:padded_size + image_col] = image #Matriz de imagen con padding.
    print("Padded image:")
    print(padded_image)

    
    return padded_image
    #Padding