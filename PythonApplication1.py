import re
import numpy
import cv2
from matplotlib import pyplot

def resize(img, x, y):
    result = cv2.resize(img, None,fx=x, fy=y, interpolation = cv2.INTER_AREA)
    return result

def expand(img, x, y):
    return resize(img, x, y)

def shrink(img, x, y):
    return resize(img, 1/x, 1/y)

def transpose(img):
    return img.T

def blur(img, x, y):
    return cv2.blur(img,(x, y))

def threshold(img):
    ret, resultImage = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    return resultImage

def dark(img):

    len1 = len(img)
    for i in range(len1):
        len2 = len(img[i])
        for j in range(len2):
            len3 = len(img[i][j])
            for k in range(len3):
                value = img[i][j][k]
                if value > 20:
                    img[i][j][k] = img[i][j][k] - 20

    return img;

def main():
    img = cv2.imread('imagem.pgm')
    pyplot.imshow(img, pyplot.cm.gray)
    pyplot.show()
    
    while True:
            option = input("Choose a option: \n 1 - transpose \n 2 - expand \n 3 - shrink \n 4 - blur \n 5 - threshold binary \n 6 - to the dark \n Else - break \n")

            if option == '1':
                img = transpose(img)
            
            elif option == '2':
                x = int(input("Input x scale: "))
                y = int(input("Input y scale: "))
                img = expand(img, x, y)

            elif option == '3':
                x = int(input("Input x scale: "))
                y = int(input("Input y scale: "))
                img = shrink(img, x, y)

            elif option == '4':
                x = int(input("Input x scale: "))
                y = int(input("Input y scale: "))
                img = blur(img, x, y)

            elif option == '5':
                img = threshold(img)

            elif option == '6':
                img = dark(img)

            else:
                break

            pyplot.imshow(img, pyplot.cm.gray)
            pyplot.show()
            cv2.imwrite('newimage2.png', img)

if __name__ == "__main__":
    main()