"""
1 - veri isimli bir klasör oluştur.
2 - zip dsosyasını veri klasörüne çıkart.
3 - zip dosyası içindeki csv dosyalarının tüm içeriğini tek bir csv dosyasında birleştir, volume olmasın.
4 - bu kayıtların tamamını sqlite veritabanına bir tablo oluşturarak yükle.
5 - kullanıcının belirlediği paritenin
    kullanıcının belirlediği aralığının
    kullanıcının belirlediği değerin
    grafiğini çizdir (veriler sqlite tan çekilecek).
"""
import os
import zipfile
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

bag = sqlite3.connect("kripto.vt")
cursor = bag.cursor()


parite = "AVAXUSDT"  # input("Parite Giriniz :")
bas_tarih = "2022-02-03"  #  input("Başlangıç Tarihi :")
bit_tarih = "2022-02-04"  # input("Bitiş Tarihi :")

sorgu = "SELECT * FROM parite WHERE " \
        "(otime BETWEEN '"+bas_tarih+"' " \
        "AND '"+bit_tarih+"') " \
        "AND parite='"+parite+"'"
cursor.execute(sorgu)
sonuc = cursor.fetchall()
liste_x = []
liste_y = []
for mum in sonuc:
    #print(mum)
    #print(mum[1])
    liste_y.append(mum[6])
    liste_x.append(mum[2])

plt.plot(liste_x, liste_y)
plt.show()
bag.close()