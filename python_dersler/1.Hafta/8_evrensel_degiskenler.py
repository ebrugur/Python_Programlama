x = 3
def y():
    x = 6
    print(x)

y()
print(x)

def z():
    global x
    x = 6
    print(x)

z()
print(x)