sozluk = {
  "marka": "Ford",
  "model": "Fiesta",
  "yil": 2020
}

print(sozluk)
print(sozluk["marka"])
print(sozluk["model"])
print(sozluk["yil"])

sozluk["renk"] = "mavi"
print(sozluk)
print(sozluk["renk"])
sozluk["renk"] = "mor"
print(sozluk)

print(sozluk.keys())
print(sozluk.values())

for i in sozluk.keys():
    print(i, ":", sozluk[i])