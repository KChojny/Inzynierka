from PIL import Image
import numpy as np


import file
import num2YCbCr
import axis_plus
import resolution
import blocks

#konwersja obrazu
print("Konwersja obrazu na warosci liczbowe")
obrazek = "lena.png"
#obrazek = "serce.jpg"
img = Image.open(obrazek)
I = np.array(img)

#tworzenie macierzy dla YCbCr
print("Tworzenie macierzy YCbCr")
Y = np.zeros((int(img.size[0]), int(img.size[1])))
Cb = np.zeros((int(img.size[0]), int(img.size[1])))
Cr = np.zeros((int(img.size[0]), int(img.size[1])))

#zapisywanie do macierzy wartosci
num2YCbCr.YCbCr(I,Y,Cb,Cr)

#luminancja
file.save(Y,"Y")

#chrominancja niebieskiego
file.save(Cb,"Cb")

#chrominancja czerwonego
file.save(Cr,"Cr")

print("Sprawdzenie zgodnosci macierzy")
#dodawanie kolumny i macierzy
if(img.size[0] % 2 != 0 or img.size[1] % 2 != 0):
    num1 = 2 - (img.size[0] % 2)
    num2 = 2 - (img.size[1] % 2)
    new_Cb = np.zeros((int(Cb.shape[0] + num1), int(Cb.shape[1]+ num2)))
    axis_plus.add_col_row(Cb, new_Cb, num1, num2)
    new_Cr = np.zeros((int(Cr.shape[0] + num1), int(Cr.shape[1] + num2)))
    axis_plus.add_col_row(Cr, new_Cr, num1, num2)
    Cb = new_Cb
    Cr = new_Cr

    #chrominancja niebieskiego
    file.save(new_Cb,"Cb+")

    #chrominancja czerwonego
    file.save(new_Cr,"Cr+")

Cb2 = np.zeros((int(Cb.shape[0]/2), int(Cb.shape[1]/2)))
resolution.subsampling(Cb, Cb2)
Cr2 = np.zeros((int(Cr.shape[0]/2), int(Cr.shape[1]/2)))
resolution.subsampling(Cr, Cr2)

#chrominancja niebieskiego
file.save(Cb2,"Cb2")

#chrominancja czerwonego
file.save(Cr2,"Cr2")

print("Sprawdzenie zgodnosci macierzy")
if(Y.shape[0] % 8 != 0 or Y.shape[1] % 8 != 0):
    num1 = 8 - (Y.shape[0] % 8)
    num2 = 8 - (Y.shape[1] % 8)
    new_Y = np.zeros((int(Y.shape[0] + num1), int(Y.shape[1]+ num2)))
    axis_plus.add_col_row(Y, new_Y, num1, num2)
    Y = new_Y
    file.save(Y,"Y+")

if(Cb2.shape[0] % 8 != 0 or Cb2.shape[1] % 8 != 0):
    num1 = 8 - (Cb2.shape[0] % 8)
    num2 = 8 - (Cb2.shape[1] % 8)
    new_Cb2 = np.zeros((int(Cb2.shape[0] + num1), int(Cb2.shape[1]+ num2)))
    axis_plus.add_col_row(Cb2, new_Cb2, num1, num2)
    new_Cr2 = np.zeros((int(Cr2.shape[0] + num1), int(Cr2.shape[1] + num2)))
    axis_plus.add_col_row(Cr2, new_Cr2, num1, num2)
    Cb2 = new_Cb2
    Cr2 = new_Cr2
    file.save(Cb2,"Cb2+")
    file.save(Cr2,"Cr2+")

print("Dzielenie macierzy na bloki")
blocks.b8x8(Y)
