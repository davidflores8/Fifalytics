from cgitb import text
import cv2
from cv2 import CALIB_HAND_EYE_ANDREFF
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Prestamo\AppData\Local\Programs\Tesseract-OCR\tesseract"

image= cv2.imread("./Fotos Proyecto Inteligentes/verrati.png")
texto=pytesseract.image_to_string(image, lang=None)
cadena=""
for i in texto:
    if i.isdigit():
        cadena+=str(i)
print (cadena)
print (texto)
cv2.imshow("image: ", image)
cv2.waitKey(0)
cv2.destroyAllWindows()