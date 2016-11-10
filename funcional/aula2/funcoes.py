def cria_imposto(aliquota):
    def imposto(valor):
        return aliquota * valor
    return imposto

def cria_imposto2(aliquota):
    def imposto(valor):
        return lambda valor : aliquota * valor
