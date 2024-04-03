Algoritmo de Euclides
a = int(input("Dame primer número: "))
b = int(input("Dame segundo número: "))

def euclides(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        r = a % b
        return euclides(b, r)

print("El MCD de", a, "y", b, "es:", euclides(a, b))
