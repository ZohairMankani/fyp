# -*- coding: utf-8 -*-
"""ocr_helper.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Z4EQRinrXKCl701yugkgUidkPw9POuE3
"""

import pytesseract
import cv2

def extract_text_from_image(image):
    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    extracted_text = pytesseract.image_to_string(gray)
    return extracted_text