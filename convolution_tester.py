# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 16:24:57 2021

@author: Okale
"""
import numpy as np
import matplotlib.pyplot as plt

def complete_byte(bits):
    if len(bits) < 8:
        while(len(bits)<8):
            bits = "0" + bits
        byte = bits
    else:
        byte = bits
            
    return byte

def int_convert(fp):
    #separa los bits en sus respectivos campos
    s = fp[0]
    #print("Signo: ",s)
    exp = fp[1:9]
    #print("Exp: ",exp)
    man = fp[9:]
    #print("Mantissa: ",man)
    #desbiasa el exponente
    exp = int(exp,2) - 127
    #print(exp)
    #Convierte la mantisa en una lista iterable
    man = list(man)
    man = np.array(man,dtype=np.float64)
    #Decimales de cada bit
    f_bits = [0.5,0.25,0.125,0.0625,0.03125,0.015625,0.0078125,0.00390625,0.001953125,0.0009765625,0.00048828125,0.000244140625,0.0001220703125,0.00006103515625,0.000030517578125]
    f_bits = np.array(f_bits)
    #Realiza la multiplicación de la mantisa con los decimales de cada bit
    n_dec = 1 + sum(f_bits * man)
    n_dec = n_dec * (2**exp)
    n_dec = n_dec #round(n_dec * 255)
    if s == 1:
        n_dec = n_dec * -1
        
    return n_dec  

img = [[0x3fd546,0x3fc6ff,0x3fe37f,0x3fc70d,0x3fc3c3,0x3fa3f9,0x3fa3f9,0x3f8ae0],
       [0x3fce22,0x3fb8c6,0x3fd546,0x3fbff8,0x3fd1fc,0x3fc06a,0x3fcb4a,0x3fb231],
       [0x3fdc5b,0x3fce23,0x3fdc6a,0x3fc71c,0x3fc71c,0x3fb58a,0x3fc06a,0x3fb232],
       [0x3fc70e,0x3fb8d5,0x3fbff8,0x3fb1bf,0x3fb8d5,0x3fb1b1,0x3fbc91,0x3fbc91],
       [0x3fb8e3,0x3fbff8,0x3fb1bf,0x3fb1b1,0x3fa378,0x3fa735,0x3fae58,0x3fb56e],
       [0x3f9c71,0x3faa9c,0x3f9c63,0x3fa36a,0x3f9c55,0x3fb92a,0x3fc771,0x3fd59b],
       [0x3faa9c,0x3fb8c6,0x3fa378,0x3fa36a,0x3f953f,0x3fb5e0,0x3fcb4a,0x3fe08a],
       [0x3f9c63,0x3fa378,0x3f9c63,0x3f9c55,0x3f9c55,0x3fb92a,0x3fc771,0x3fd59b]]

for i in range(8):
    for j in range(8):
        fp_number = bin(img[i][j]).replace("b","0")
        img[i][j] = int_convert(fp_number)
        
fpga = np.array(img,dtype=np.float32)
plt.imshow(fpga,cmap="gray")
plt.show()
np.save("conv_fpga.npy",fpga)
#img = img.reshape((64,))

#img = fp.int_convert(img)

        