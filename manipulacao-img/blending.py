import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def showImage(img):
    imgMPLIB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    plt.imshow(imgMPLIB)
    plt.show()

def addImageOverlay(background, foreground, translationForegroundW, translationForegroundH):
    backH, backW, _ = background.shape
    foreH, foreW, _ = foreground.shape
    remainingH, remainingW = backH - foreH, backW - foreW

    if translationForegroundH + foreH > backH:
        print("Erro: sobreposição com altura maior do que a permitida.")
        print("Posição final que altura do objeto da frente termina:", translationForegroundH + foreH)
        print("Altura do fundo:", backH)
        return

    if translationForegroundW + foreW > backW:
        print("Erro: sobreposição com largura maior do que a permitida.")
        print("Posição final que largura do objeto da frente termina:", translationForegroundW + foreW)
        print("Largura do fundo:", backW)
        return

    #parte do cenário do fundo em que a imagem será adicionada
    crop = background[translationForegroundH : foreH + translationForegroundH, translationForegroundW : foreW + translationForegroundW]

    #Transformamos o foreground em imagem com tons de cinza e criamos uma máscara binária da mesma com a binarização (cv2.threshold)
    foregroundGray = cv.cvtColor(foreground, cv.COLOR_BGR2GRAY)
    ret, maskFore = cv.threshold(foregroundGray, 240, 255, cv.THRESH_BINARY)

    #Agora aplicamos uma operação de AND binário na imagem recortada 'crop'. No caso, realizar a operação binária entre a mesma imagem não terá efeito. Só que, com a inclusão da máscara no terceiro parâmetro, os pixels pretos de maskFore serão ignorados e, portanto, ficarão escuros. Com isso temos a marcação em que vamos incluir o foreground posteriormente.
    backWithMask = cv.bitwise_and(crop, crop, mask = maskFore)
    foreWithMask = cv.bitwise_not(maskFore)
    foreWithMask = cv.bitwise_and(foreground, foreground, mask = foreWithMask)

    #Faremos a composição entre 'frente' e 'fundo', compondo o foreground na imagem extraída do background.
    combinedImage = cv.add(foreWithMask, backWithMask)

    #Adicionamos a imagem gerada no background final.
    copyImage = background.copy()
    copyImage[translationForegroundH:foreH + translationForegroundH, translationForegroundW:foreW + translationForegroundW] = combinedImage

    return copyImage


def showMultipleImageGrid(imgsArray, titlesArray, x, y):
    if(x < 1 or y < 1):
        print("ERRO: X e Y não podem ser zero ou abaixo de zero!")
        return
    elif(x == 1 and y == 1):
        showImageGrid(imgsArray, titlesArray)
    elif(x == 1):
        fig, axis = plt.subplots(y)
        fig.suptitle(titlesArray)
        yId = 0
        for img in imgsArray:
            imgMPLIB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
            axis[yId].imshow(imgMPLIB)

            yId += 1
    elif(y == 1):
        fig, axis = plt.subplots(1, x)
        fig.suptitle(titlesArray)
        xId = 0
        for img in imgsArray:
            imgMPLIB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
            axis[xId].imshow(imgMPLIB)

            xId += 1
    else:
        fig, axis = plt.subplots(y, x)
        xId, yId, titleId = 0, 0, 0
        for img in imgsArray:
            imgMPLIB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
            axis[yId, xId].set_title(titlesArray[titleId])
            axis[yId, xId].imshow(imgMPLIB)
            if(len(titlesArray[titleId]) == 0):
                axis[yId, xId].axis('off')

            titleId += 1
            xId += 1
            if xId == x:
                xId = 0
                yId += 1

        fig.tight_layout(pad=0.5)
    plt.show()
    
def showImageGrid(img, title):
    fig, axis = plt.subplots()
    imgMPLIB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    axis.imshow(imgMPLIB)
    axis.set_title(title)
    plt.show()

def plotTwoImageVertical():
    imgOriginal = cv.imread('char_leage.png')
    imgReplicate = cv.copyMakeBorder(imgOriginal, 200, 100, 50, 10, cv.BORDER_REPLICATE)

    imgsArray = [imgOriginal, imgReplicate]
    title = 'Imagem original e Imagem com borda replicada'
    showMultipleImageGrid(imgsArray, title, 1, 2)

def plotTwoImageHorizontal():
    imgOriginal = cv.imread('char_leage.png')
    imgReplicate = cv.copyMakeBorder(imgOriginal, 200, 100, 50, 25, cv.BORDER_REPLICATE)

    imgsArray = [imgOriginal, imgReplicate]
    title = 'Imagem original e Imagem com borda replicada'
    showMultipleImageGrid(imgsArray, title, 2, 1)

def plotAddImages():
    circleImage = cv.imread('circle.png')
    rectangleImage = cv.imread('rectangle.png')

    circleImage.shape
    rectangleImage.shape
    
    # cv.add(primeiraImagem, segundaImagem) - Para adicionar imgs
    addedImage = cv.add(circleImage, rectangleImage)
    
    addedWeightedImage = cv.addWeighted(circleImage, 0.9, rectangleImage, 0.1, 0)

    #criando grid com 3 imagens, a segunda com borda replicada e a terceira com borda de espelho, tendo ultima imagem transparente
    imgsArray = [circleImage, rectangleImage, addedImage, addedWeightedImage]
    titlesArray = ['Círculo', 'Retângulo', 'cv.add()', 'cv.addWeightedImage']
    showMultipleImageGrid(imgsArray, titlesArray, 2, 2)

def resizeImage(image, scalePercent):
    width = int(image.shape[1] * scalePercent/100)
    height = int(image.shape[0] * scalePercent/100)
    image = cv.resize(image, (width, height))
    
    return image

def memeGeneratorWithBlending(fala1, imagem1, fala2, imagem2):
    olavoSerio = cv.imread(imagem1)
    olavoSerio = resizeImage(olavoSerio, 250)
    
    olavoPuto = cv.imread(imagem2)
    olavoPuto = resizeImage(olavoPuto, 250)
    finalImagemDoisOlavo = addImageOverlay(OlavoSerio, OlavoPuto, 930, 460, 240)
    
    finalImage = addBlending(OlavoSerio, finalImagemDoisOlavo, 0.4)
    
    finalImage = cv.putText(finalImage, fala1, (210, 420), cv.FONT_HERSHEY_SIMPLEX, 2.5, (0,0,0), 5, cv.LINE_AA)
    
    finalImage = cv.putText(finalImage, fala2, (1030, 1150), cv.FONT_HERSHEY_SIMPLEX, 2.5, (0,0,0), 5, cv.LINE_AA)

    cv.imwrite('memeolavo.png', finalImage)

    memeGeneratorWithBlending('Você é cristão de esquerda?', 'olavo-serio.png', 'ORA PORRA!', 'olavo-puto.png')

def main():
    plotAddImages()

main()
