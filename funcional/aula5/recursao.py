# n! : 1 se n == 0 se nao n * (n-1)!
# n == 0 (caso base)
# n * (n-1)! (caso recursivo)

fat = lambda n : 1 if n == 0 else n * fat(n-1)

print fat(5)

soma = lambda x : 1 if x == 1 else x + soma(x-1)

print soma(5)

math_pow = lambda x,n : 1 if n == 0 else x * math_pow(x, n-1)

print math_pow(2,3)

mdc = lambda m,n : m if n == 0 else mdc(n,m%n)

print mdc(2,6)

print "---------"

def meu_imprime_range(i , f):
    print i
    if(i == f): return
    else: imprime_range(i + 1, f)

def imprime_range_prof(i , f):
    if(i <= f):
        print i
        imprime_range_prof(i+1, f)

imprime_range_prof(3,10)

print "--------"

def tamanho(lst):
    if not lst: return 0
    else: return 1 + tamanho(lst[1:])

print tamanho([1,2,3,4])

def somal(lst):
    if not lst:
        return 0
    else:
        return lst[0] + somal(lst[1:])

print somal([2,3,4])

def membro (e, lst):
    if not lst:
        return False
    if(e == lst[0]):
        return True
    else:
        return membro(e, lst[1:])

print membro('a', 'hdhua')

def inverso(lst):
    if not lst:
        return []
    else:
        return inverso(lst[1:]) + [lst[0]]

print inverso([2,4,6,8])

def maximo (lst):
    if (len(lst) == 1): return lst[0]
    max_restante = maximo(lst[1:])
    return lst[0] if lst[0] > (max_restante) else max_restante

print maximo([2,3,4,1,9,-1,-2])

def palindromo(lst):
    if not lst: return True
    return lst[0] == lst[-1] and palindromo(lst[1:-1])

print palindromo('arara')

def intercala(lst1, lst2):
    if len(lst1) == 0 or len(lst2) == 0:  return lst1 + lst2
    if(lst1[0] < lst2[0]):
        return [lst1[0]] + [lst2[0]] + intercala(lst1[1:], lst2[1:])
    else:
        return [lst2[0]] + [lst1[0]] + intercala(lst1[1:], lst2[1:])

print intercala([1,5,7],[2,4,6])

def mergeSort(lst):
    if len(lst) <= 1 : return lst
    else:
        meio = len(lst) // 2
        esquerda = lst[:meio]
        direita = lst[meio:]
        esquerda = mergeSort(esquerda)
        direita = mergeSort(direita)
        return intercala(esquerda, direita)

print mergeSort([2,4,1,10,9,7])
