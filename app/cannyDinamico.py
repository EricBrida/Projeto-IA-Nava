import cv2
import numpy as np

def cannyDinamico(imagem, sigma=0.33):
    mediana = np.median(imagem)

    minVal = int(max(0, (1.0 - sigma) * mediana))
    maxVal = int(min(255, (1.0 + sigma) * mediana))

    bordas = cv2.Canny(imagem, minVal, maxVal)

    return bordas