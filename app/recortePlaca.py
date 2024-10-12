import cv2
from app.preProcessamento import *

def encontraPlaca(imagem):
    
    # Linha para teste de recebimento da imagem
    # cv2.imshow('img', imagem)

    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    _, imagem_binary = cv2.threshold(imagem_cinza, 90, 255, cv2.THRESH_BINARY)

    # Linha para gerar um desfoque na imagem
    imagem_melhorada = cv2.GaussianBlur(imagem_binary, (5, 5), 0)
    
    contornos, hier = cv2.findContours(imagem_melhorada, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for contorno in contornos:
        perimetro = cv2.arcLength(contorno, True)

        if perimetro > 120:
            aproxx = cv2.approxPolyDP(contorno, 0.03 * perimetro, True)

            if len(aproxx) != 4:
                continue

            (x, y, alt, lar) = cv2.boundingRect(contorno)
            cv2.rectangle(imagem, (x, y), (x + alt, y + lar), (0, 255, 0), 2)

            placa = imagem[y: y + lar, x: x + alt]

            cv2.imwrite('img\output\placa\placa.jpg', placa)

            if placa is None:
                return
            
            preProcessamentoPlaca(placa)


    cv2.waitKey(0)
    cv2.destroyAllWindows()