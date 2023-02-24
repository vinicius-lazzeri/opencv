import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def showImage(img):
    imgMPLIB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    plt.imshow(imgMPLIB)
    plt.show()

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

def plotThreeImages():
    imgOriginal = cv.imread('char_leage.png')
    imgReplicate = cv.copyMakeBorder(imgOriginal, 100, 100, 100, 100, cv.BORDER_REPLICATE)
    imgReflect = cv.copyMakeBorder(imgOriginal, 100, 100, 100, 100, cv.BORDER_REFLECT)
    imgTransparent = np.ones((imgOriginal.shape[0], imgOriginal.shape[1], 4), np.uint8) * 255

    imgsArray = [imgOriginal, imgReplicate, imgReflect, imgTransparent]
    titlesArray = ['Original', 'Borda Replicada', 'Borda de Espelho', '']
    showMultipleImageGrid(imgsArray, titlesArray, 2, 2)

def plotFourImages():
    imgOriginal = cv.imread('char_leage.png')
    imgReplicate = cv.copyMakeBorder(imgOriginal, 100, 100, 100, 100, cv.BORDER_REPLICATE)
    imgReflect = cv.copyMakeBorder(imgOriginal, 100, 100, 100, 100, cv.BORDER_REFLECT)
    imgReflect101 = cv.copyMakeBorder(imgOriginal, 100, 100, 100, 100, cv.BORDER_REFLECT_101)
    

    imgsArray = [imgOriginal, imgReplicate, imgReflect, imgReflect101]
    titlesArray = ['Original', 'Borda Replicada', 'Borda de Espelho', 'Espelho R101']
    showMultipleImageGrid(imgsArray, titlesArray, 2, 2)

def plotSixImages():
    imgOriginal = cv.imread('char_leage.png')
    imgReplicate = cv.copyMakeBorder(imgOriginal, 100, 100, 100, 100, cv.BORDER_REPLICATE)
    imgReflect = cv.copyMakeBorder(imgOriginal, 100, 100, 100, 100, cv.BORDER_REFLECT)
    imgReflect101 = cv.copyMakeBorder(imgOriginal, 100, 100, 100, 100, cv.BORDER_REFLECT_101)
    imgWrap = cv.copyMakeBorder(imgOriginal, 100, 100, 100, 100, cv.BORDER_WRAP)

    BLUE = [255, 0, 0]
    imgConstant = cv.copyMakeBorder(imgOriginal, 100, 100, 100, 100, cv.BORDER_CONSTANT, value = BLUE)

    imgsArray = [imgOriginal, imgReplicate, imgReflect, imgReflect101, imgConstant, imgWrap]
    titlesArray = ['Original', 'Borda Replicada', 'Borda de Espelho', 'Espelho R101', 'Moldura', 'Efeito Wrap']
    showMultipleImageGrid(imgsArray, titlesArray, 3, 2)
    
def main():
    plotSixImages()

main()
