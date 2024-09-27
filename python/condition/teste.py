def calcular(*args):
    r = sum(args)
    for i in args:
        r += i
    return r

res = calcular(1,4,5)
print(res)