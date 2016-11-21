# quadrados dos naturais que sao pares
# {n**2 | n pertence a N e n eh par}
# list compreehension

# lista = [n**2 for n in range(10) if n % 2 == 0]
# equivalente a
# lista = filter(lambda x: x%2 == 0, map(lambda x: x*x , range(10)))

# dominios sao definidos como
# for variavel in { colecao }

# 2 - Quais os quadradaos de uma lista de 1 a 20 que sao pares e menores que 100

lista = [n**2 for n in range(21) if n**2 % 2 == 0 and n**2 < 100]

# 1) descreva com LC
# map(f,l)
# filter(f,l)
# filter(f2 , map(f1,l))

lista = range(20)

print "lista original \n", lista

quadrado = lambda x : x**2
ehPar = lambda x : x % 2 == 0
maiorQueCem = lambda x : x > 100

print map(quadrado, lista)
print [quadrado(x) for x in lista]

print filter(ehPar, lista)
print [x for x in lista if ehPar(x)]

print filter(maiorQueCem, map(quadrado, lista))
print [quadrado(x) for x in lista if maiorQueCem(quadrado(x))]

# inverte
inverte = lambda L : [L[-i] for i in range(1, len(L) + 1)]
print inverte(lista)

def sovogais(palavra):
    # return not any([c not in 'aeiou' for c in palavra])
    # return len([c for c in palavra if c not in 'aeiou']) == 0
    return all([c in 'aeiou' for c in palavra])

def ordenada(L):
    #return len([i for i in range(len(L) - 1) if L[i] > L[i+1]]) == 0
    return all([L[i] < L[i+1] for i in range(len(L) - 1)])
palavras = ['aaaa', 'abaa', 'xaed', 'aeo']

print map(sovogais, palavras)

print ordenada([1,2,3,4,5])
print ordenada([3,4,1,5])

print [n for n in range(100000) if ''.join(inverte(str(n))) ==  str(4*n)]
