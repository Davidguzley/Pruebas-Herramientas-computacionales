#Librerias para hacer uso de matrices.
import numpy as np
import cv2
import matplotlib.pyplot as plt
from padding import padding

def conv_helper(fragment, kernel):
    """ multiplica 2 matices y devuelve su suma"""
    
    f_row, f_col = fragment.shape # obtiene tupla con las medidas de alto y ancho del fragmento
    
    resultado = 0
    for row in range(f_row):
        for col in range(f_col):
            resultado += fragment[row,col] *  kernel[row,col]
    return resultado

def convolution(image, kernel):
    """Función de convolución con padding
    """

    # Analiza la imágen para que en caso de que tenga color se convierte a escala de grises, de 3 dimesiones a 2
    if len(image.shape) == 3: #De 3 dimenciones
        print("Dimenciones de imagen: {}".format(image.shape))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #Se cambia a dos dimenciones
        print("Nuevas dimenciones: {}".format(image.shape))
    else:
        print("Dimenciones de imagen: {}".format(image.shape))

    # Tamaño del filtro
    print("Kernel Shape : {}".format(kernel.shape))

    # Impresión de filtro kernel
    print('Kernel')
    for row in kernel:
            for col in row:
                print(col ,end=' ')
            print(end='\n')

    image_row, image_col = image.shape # Obtiene una tupla y asigna alto y ancho de la imagen. 
    kernel_row, kernel_col = kernel.shape # Obtiene una tupla y asigna alto y ancho del filtro.

    output_x = (image_col - (kernel_col / 2) * 2) + 1 #Asigna el ancho del output en base al filtro.
    output_y = (image_row - (kernel_row / 2) * 2) + 1 #Asigna el alto del output en base al filtro.

    output = np.zeros([int(output_y), int(output_x)]) # Matriz donde se guarda el resultado.

    # (filas o columnas - 1) / 2
    padded_size = int((kernel_row - 1) / 2) #Tamaño de padding

    #Obtenemos la imagen con padding
    padded_image = padding(image,padded_size)

    #  Multiplica la matriz de image con la de kernel y devuelve la suma de esta con conv_helper
    for row in range(int(output_y)):
        for col in range(int(output_x)):
            output[row, col] = conv_helper(
                                padded_image[row:row + kernel_row, 
                                col:col + kernel_col], kernel)

    return output