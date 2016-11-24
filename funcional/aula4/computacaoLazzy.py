# computacao em demanda

primo = lambda n : True not in (n%k == 0 for k in range(2,n))

# (n for k in range(k)) -> n eh um iterador, a estrutura inteira eh um gerador
# executa a computacao um elemento de cada vez

print primo(1021)

gerador = (n*n for n in range(10))

print next(gerador)
print next(gerador)
print next(gerador)
print next(gerador)

print list(gerador) # ja consumiu G

# alta ordem: map, filter, reduce (ordem arbitraria de execucao)
# muito bom para paralelizacao

# iteradores, geradores e streams (execucao preguicoca, sequencial)
