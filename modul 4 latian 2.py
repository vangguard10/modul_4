# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 08:26:21 2022

@author: fariz
"""
import calendar as c
print("Program dapat menentukan jumlah hari di salah satu bulan")
respon = "y"
while respon == "y": 
    tahun = int(input("Masukan Tahun: ")) 
    bulan = int(input("Masukan Bulan: "))
    print("Ada", (c.monthrange(tahun, bulan)[1]), "Hari di bulan ke",bulan)
    respon = input("ketik'y' jika ingin lanjut, ketik 'n' jika stop ")
    if respon == "n":
        print("Terimakasih sudah Menggunakan program ini")
        print("Alfarizqi Wira Anadyar 065002200034")
        break