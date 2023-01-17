liste = ["Telefon", "Bilgisayar", "Tablet"]

liste.sort()
print(liste)

liste.reverse()
print(liste)

def fonksiyon(n):
  return abs(n - 90)

sayi_listesi = [1000, 80, 95, 74, 130]
sayi_listesi.sort(key=fonksiyon)
print(sayi_listesi)