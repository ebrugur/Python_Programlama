def ne_varsa_topla(*a):
    toplam = 0
    for deger in a:
        toplam += deger
    return toplam


print(ne_varsa_topla(9, 12, 23, 17.8, 99))