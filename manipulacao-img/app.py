import numpy as np
import cv2

def showImage(img):
    # Biblioteca que funciona melhor com manipulação de gráficos (toda imagem é uma matriz e portanto um gráfico)
    from matplotlib import pyplot as plt

    # Convertendo as cores 'vanilla' BGR para RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Comando para exibir a imagem.
    plt.imshow(img)
    plt.show()

def getColor(img, x, y):
    return img.item(y, x, 0), img.item(y, x, 1), img.item(y, x, 2)

def setColor(img, x, y, b, g, r):
    img.itemset((y, x, 0), b)
    img.itemset((y, x, 1), g)
    img.itemset((y, x, 2), r)

    return img

def main():
    # Comando para carregar imagem
    obj_img = cv2.imread('image.jpeg')
    #print(obj_img.shape) #AlturaxLarguraXCanais de cor na imagem.
    # Podendo retornar na variável abaixo como neste exemplo:
    altura, largura, canais_de_cor = obj_img.shape
    print(f'[Dimensões da imagem LxA]\n{largura}x{altura}\nCanais de cores: {canais_de_cor}')

    #Manipulando pixels
    for y in range(0, altura):
        for x in range(0, largura):
            #azul, verde, vermelho = obj_img[y][x]
            #Como aqui em baixo:
            #print(f'[{str(x)} {str(y)}] = {obj_img[y][x]}')
            #input()
        
            azul, verde, vermelho = getColor(obj_img, x, y)
            obj_img = setColor(obj_img, x, y, verde, azul, vermelho)
            #1380, 790
        #cv2.imwrite('char_leage.png', obj_img)
    eye_img = obj_img[573:573 + 40, 462:462 + 70]
    showImage(eye_img)
    obj_img[1380:1380 + eye_img.shape[0], 790: 790 + eye_img.shape[1]] = eye_img
    showImage(obj_img)
main()
