def benim_fonksiyonum(n):
  return lambda a: a * n

kat_al = benim_fonksiyonum(3)
print(kat_al(8))

kat_al = benim_fonksiyonum(8)
print(kat_al(8))