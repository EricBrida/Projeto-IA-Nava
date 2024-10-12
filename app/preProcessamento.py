import cv2
from app.ocrPlaca import *

def preProcessamentoPlaca(placa):
    
    placa_resize = cv2.resize(placa, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC)

    placa_cinza = cv2.cvtColor(placa_resize, cv2.COLOR_BGR2GRAY)

    _, placa_binary = cv2.threshold(placa_cinza, 70, 255, cv2.THRESH_BINARY)
    cv2.imshow('placa_binary',placa_binary)

    if placa_binary is None:
        raise ValueError('A imagem "placa_binary" está vazia ou corrompida')
    
    cv2.imwrite('img\output\placaOCR\placaprocessada.png', placa_binary)

    ocrPlacaFinal(placa_binary)

    cv2.waitKey(0)
    cv2.destroyAllWindows()