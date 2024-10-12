import pytesseract

def ocrPlacaFinal(placa_ocr):
    # Configuração básica para o funcionamento do tesseract
    config = r'-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 --psm 8 --oem 3'

    saida = pytesseract.image_to_string(placa_ocr, lang="eng", config=config)
    
    if len(saida.strip()) != 7:
        print(f'Placa não encontrada ou valor obtido de forma erronea, placa obtida: {saida}')
    else:
        print(f'O resultado da placa do carro é: {saida}')