"""
Kendisine gönderilen sayılardan sadece palindrom olanları toplayan diğerlerini de bu toplamdan çıkaran ve geri
döndüren python fonksiyonunu yazınız.
"""
def palinDROM(*drom):
    toplam = 0
    for sayi in drom:
        if str(sayi) == str(sayi)[::-1]:
            toplam += sayi
        else:
            toplam -= sayi
    return toplam


print(palinDROM(11, 202, 66, 40, 6006))