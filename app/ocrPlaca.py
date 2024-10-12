import pytesseract

def ocrPlacaFinal(placa_ocr):
    # Configuração básica para o funcionamento do tesseract
    config = r'-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 --psm 6'

    saida = pytesseract.image_to_string(placa_ocr, lang="eng", config=config)
    
    if saida is None:
        raise ValueError('Não foi possível fazer o reconhecimento da placa')
    
    print(f'O resultado da placa do carro é: {saida}')