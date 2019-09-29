
from PIL import Image
import pytesseract as ocr

# Abre as imagens
#back = Image.open("teste.jpg") #Fundo
imagem = ocr.image_to_string(Image.open("teste.jpg"),lang='por')
print (imagem)
