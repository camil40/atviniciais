tupla = (1,4,6)

tupla = list(tupla)
tupla.pop()
tupla.append(3)

tupla = tuple(tupla)
print(tupla)


tu = (1,2,10)
tu = list(tu)
tu[2] = 3
tu = tuple(tu)
print(tu)