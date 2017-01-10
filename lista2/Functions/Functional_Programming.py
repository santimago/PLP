from math import sqrt

lst = [3, 4, 1, 2, 1, 2, 2, 2]


# 3) Verificar lista com itens duplicados.
def tem_duplicatas(lst):
    if len(lst) < 2:
        return False
    elif lst[0] in lst[1:]:
        return True
    else:
        return tem_duplicatas(lst[1:])


#print tem_duplicatas(lst)


# 4) Remover itens duplicados de uma lista, mantem apenas a ultima ocorrencia
def remove_duplicatas(lst):
    if len(lst) < 2:
        return lst
    elif lst[0] in lst[1:]:
        return remove_duplicatas(lst[1:])
    else:
        return [lst[0]] + remove_duplicatas(lst[1:])


print remove_duplicatas(lst)


# 5) triada
def triade(n, m):
    l = range(n, m+1)
    return [(a,b,c) for a in l for b in l for c in l if a*a + b*b == c*c]

print triade(1,10)

# 6)

lst2 = [4, 7, 8, 2, 1]

#print map(lambda n: n+2, filter(lambda m: m>3, lst2))


# 7)
def sum(lst):
    if not lst:
        return 0
    elif len(lst) == 1:
        return lst[0]
    else:
        return lst[0] + sum(lst[1:])


sqrta = lambda l: [sqrt(x) for x in l]


def mapseq(fs, arg):
    if len(fs) < 2:
        return fs[0](arg)
    else:
        return fs[0](mapseq(fs[1:], arg))


# print mapseq([sqrt, sum, lambda l: [x*x for x in l]], range(5))


#8)
def printf(arg):
    print arg
    return arg


def repeatf(n, fs, arg):
    arg = mapseq(fs, arg)
    if n == 0:
        return
    else:
        return repeatf(n - 1, fs, arg)


#repeatf(4, [lambda n: n-1, printf], 5)


"""
def myFilter(c, L):
    if not L:
        return []
    else:
        return [L[0]] + myFilter(c, L[1:]) if c(L[0]) else myFilter(c, L[1:])

print myFilter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])
"""
