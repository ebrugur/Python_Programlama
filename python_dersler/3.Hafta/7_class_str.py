class sinif:
    metin = ""
    def __init__(self, a):
        self.metin = a

    def __str__(self):
        return "Çıktı : " + self.metin

nesne = sinif("Python")
print(nesne)