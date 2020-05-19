from PIL import Image
import numpy as np

import file
import num2YCbCr
import col_row_plus
import resolution
import quantization
import blocks
import entropy_encoding

#konwersja obrazu
print("Konwersja obrazu na wartosci liczbowe")
obrazek = "lena.png"
#obrazek = "serce.jpg"
img = Image.open(obrazek)
I = np.array(img)
QL = 50

#tworzenie macierzy dla YCbCr
print("Tworzenie macierzy YCbCr")
Y = np.zeros((int(img.size[0]), int(img.size[1])))
Cb = np.zeros((int(img.size[0]), int(img.size[1])))
Cr = np.zeros((int(img.size[0]), int(img.size[1])))

#zapisywanie do macierzy wartosci
num2YCbCr.YCbCr(I,Y,Cb,Cr)

file.save(Y,"Y")
file.save(Cb,"Cb")
file.save(Cr,"Cr")

#walidacja
col_row_plus.validation(Cb,2)
col_row_plus.validation(Cr,2)

file.save(Cb,"Cb+")
file.save(Cr,"Cr+")

#podprobkowanie
Cb2 = resolution.subsampling(Cb)
Cr2 = resolution.subsampling(Cr)

file.save(Cb2,"Cb2")
file.save(Cr2,"Cr2")

#walidacja
col_row_plus.validation(Y,8)
col_row_plus.validation(Cb2,8)
col_row_plus.validation(Cr2,8)

file.save(Y,"Y+")
file.save(Cb2,"Cr2+")
file.save(Cr2,"Cb2+")

print("Tworzenie tablicy kwantyzacji")
QTY = quantization.tables(np.zeros((8,8)), 'Y', QL)
QTC = quantization.tables(np.zeros((8,8)), 'C', QL)

print("Utworzenie tablic dla stalych transformat")
DCY = np.zeros(int(Y.shape[0] / 8) * int(Y.shape[1] / 8))
DCCr = np.zeros(int(Cr2.shape[0] / 8) * int(Cr2.shape[1] / 8))
DCCb = np.zeros(int(Cb2.shape[0] / 8) * int(Cb2.shape[1] / 8))

print("Utworzenie tablic dla zmiennych transformat")
ACY = np.zeros(int(Y.shape[0] / 8) * int(Y.shape[1] / 8), 63)
ACCr = np.zeros(int(Cr2.shape[0] / 8) * int(Cr2.shape[1] / 8), 63)
ACCb = np.zeros(int(Cb2.shape[0] / 8) * int(Cb2.shape[1] / 8), 63)

print("Dzielenie macierzy na bloki")
blocks.encoding(Y,'Y',QTY,DCY,ACY)

print("Tworzenie wektorow przyrostu")
diff = entropy_encoding.diff(DCY)

print(ACY[0][0])

'''
print("Kompresowanie stalych transformat")
compressed_file = open("compressed file.txt","a")
entropy_encoding.compresionDC(compressed_file,diff)
compressed_file.close()
'''
