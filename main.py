#Librerias
import numpy as np
import cv2
import matplotlib.pyplot as plt
from convolution import convolution

if __name__ == '__main__':

    #Se obtiene la imagen con cv2
    print("Escribe el nombre de una imagen con su extensión que esté en la carpeta del proyecto:")
    image = cv2.imread(input())
    RGB_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #convierte el espectro de color a RGB.

    # Muestra la imagen original por un plot.
    plt.imshow(RGB_img)
    plt.title("Imagen Original")
    plt.show()

    filtros = """
Aplicar filtro
1.- Edge detection
2.- Sobel
3.- Line Detection Horizontal
4.- Cambiar de imagen
5.- Salir                 
            """

    pop = True #Breack del ciclo while.
    while pop == True: #Ciclo while para imprimir filtros, cambiar imagen o salir.
        print(filtros)
        print("Elige una opcion:")
        op = input()

        if op == "1":
            edgeDetection = np.array([[-1, -1, -1],
                                    [-1, 8, -1],
                                    [-1, -1, -1]])
            imageEdge = convolution(image,edgeDetection) # Función de convolución con padding
            # Mostrar el plot del resultado con filtro.
            plt.imshow(imageEdge, cmap= 'twilight_shifted')
            edge_row, edge_col = imageEdge.shape
            plt.title("Output Edge detection of {}X{}".format(edge_row, edge_col))
            plt.show()
        elif op == "2":
            sobel= np.array([[-1,0,1],
                            [-2,0,2],
                            [-1,0,1]])
            imageSobel = convolution(image,sobel) # Función de convolución con padding
            # Mostrar el plot del resultado con filtro.
            plt.imshow(imageSobel, cmap= 'twilight_shifted')
            sobel_row, sobel_col = imageSobel.shape
            plt.title("Output Sobel of {}X{}".format(sobel_row, sobel_col))
            plt.show()
        elif op == "3":
            lineDetection = np.array([[-1,-1,-1],
                                    [2,2,2],
                                    [-1,-1,-1]])
            imageLine = convolution(image,lineDetection) # Función de convolución con padding.
            # Mostrar el plot del resultado con filtro.
            plt.imshow(imageLine, cmap= 'twilight_shifted')
            line_row, line_col = imageLine.shape
            plt.title("Output Line Detection Horizontal of {}X{}".format(line_row, line_col))
            plt.show()
        elif op == "4":
            #Se obtiene la imagen con cv2 y la convierte a una matriz de 3 dimensiones rgb.
            print("Escribe un nuevo nombre de una imagen que este en la carpeta del proyecto:")
            image = cv2.imread(input())
            RGB_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #convierte el espectro de color a RGB.

            # Muestra la imagen original por un plot.
            plt.imshow(RGB_img, cmap= 'twilight_shifted')
            plt.title("Imagen Original")
            plt.show()
        elif op == "5":
            pop = False
        else:
            print("Opción inválida")
    #Termina el ciclo while