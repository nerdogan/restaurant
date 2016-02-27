from PIL import Image
import pytesseract as tess

"""print image_to_string(Image.open('test.png'))"""
print tess.image_to_string(Image.open('image.bmp'))
