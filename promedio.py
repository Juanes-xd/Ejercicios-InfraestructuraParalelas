def promedio(valor1, valor2, valor3):
    lista = [valor1, valor2, valor3]
    return sum(lista) / len(lista)


p=0.967
s=30
operacion1 = 1-p
operacion2 = p/s
def speedUp():
    result = 1/(operacion1 + operacion2)
    return result
print(speedUp())



def speedUp2():
    result = 1/15.1929980913798
    return result
print(speedUp2())


def eficiencia():
    result = speedUp2()/s
    return result
print(eficiencia())

def amdahl():
    result = 1/((1-p) + (p/s))
    return result
#print(amdahl())