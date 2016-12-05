# [(central),[(norte),(),],[(leste),()],[(sul),()],[(oeste),()]]

mesa = [(6,6),
        [(6,5),(5,2)],
        [(6,1),(1,1),(1,5)],
        [],
        [(6,4),(4,2)]]

mesa2 = [(6,6),
        [],
        [],
        [],
        [(6,4)]]

mesa3 = [(6,6),
        [],
        [],
        [],
        [(6,3)]]

print "mesa 1 -> ", mesa
print "mesa 2 -> ", mesa2
print "mesa 3 -> ", mesa3


norte = lambda cfg: cfg[1]
primpedra = lambda cfg: cfg[0]
sul = lambda cfg: cfg[2]
oeste = lambda cfg: cfg[4]
leste = lambda cfg: cfg[3]
ponta = lambda braco: braco[-1]

pontas = lambda cfg: [ponta(braco) for braco in cfg[1:] if braco]

#print norte(mesa)
#print pontas(mesa)

valorP = lambda (a, b): b + a if b == a else b

#print valorP((1,3))

bracos_existentes = lambda cfg : filter(lambda braco : True if braco else False, cfg[1:])


#print qtd_bracos(mesa)

def todas_as_pontas(cfg):
    pts = pontas(cfg)
    return pts + [primpedra(cfg)] if len(pts) == 1 else pts

# print todas_as_pontas(mesa2)

def pontas_disponiveis(cfg):
    pts = pontas(cfg)
    return pts + [primpedra(cfg)] if len(pts) < 4 else pts


def pontosDomino(cfg):
    vtotal = sum([valorP(p) for p in todas_as_pontas(cfg)])
    return vtotal if vtotal % 5 == 0 else 0

print pontosDomino(mesa3)

'''
imprimir todas as configuracoes possiveis resultantes da insercao de uma
pedra
'''
def configuracoesAposJogar(cfg, pedra):
    pontas_dis = pontas_disponiveis(cfg)
    for p in pontas_dis:
        if(p[1] == pedra[0] or p[1] == pedra[])
    print pontas_dis

configuracoesAposJogar(mesa,(6,2))
