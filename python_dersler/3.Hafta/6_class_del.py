class sinif:
    metin = ""
    def __init__(self, a):
        self.metin = a

    def __del__(self):
        print("Silindi")

nesne = sinif("Python")
del nesne