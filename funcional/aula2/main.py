from funcoes import *

def maior(a, b):
    return a if a > b else b

def par_e_quadrado_maior_que_100(x):
    return x % 2 == 0 and x*x > 100

def maior_palavra(p1, p2):
    return p1 if len(p1) > len(p2) else p2

def divisivel_11_e_13(x):
    return x % 11 == 0 and x % 13 == 0

f = cria_imposto(.2)

print f(100)

l = [2,3,6,1,4]

# aplica a funcao em todas os elementos
print map(lambda n: n%2 == 0, l)

# apenas funcoes booleanas, retorna a lista reduzida aos elementos para os quais foi true
print filter(lambda n: n%2==0, l)

# aplica a funcao par a par, essa retorna o maior numero da lista
print reduce(maior, l)
#print reduce(lambda a, b : a if a > b else b, l)

l = range(21)

# numeros pares e com quadrado maior que 100:
l = filter(par_e_quadrado_maior_que_100,l)
l = map(lambda x: x*x , l)

print l

l = ["a1", "aa2", "0", "aaaaa5", "aaa3"]

print l

print type(l[0])

l = reduce(maior_palavra, l)

print l

# retorne o maior tamanho em uma lista de palavras

l = ["a1", "aa2", "0", "aaaaa5", "aaa3"]
l = reduce(maior_palavra, l)

print len(l)

# quantos inteiros < 100 000 sao divisiveis por 11 e 13

l = range(100001)

l = filter(divisivel_11_e_13, l)

print l

# retorne todas as palavras > k letras

k = 2

l = ["a1", "aa2", "0", "aaaaa5", "aaa3"]

l = filter(lambda palavra : len(palavra) > k, l)

print l
