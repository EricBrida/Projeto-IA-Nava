import cv2
from app.recortePlaca import *

if __name__ == '__main__':
    imagem = cv2.imread('input\carro7.jpg')
    encontraPlaca(imagem)