


def create_env():
    dic = {}
    dic['+'] = lambda x, y: x + y
    dic['-'] = lambda x, y: x - y
    dic['*'] = lambda x, y: x * y
    dic['/'] = lambda x, y: x / y
    dic['car'] = lambda x: x[0]
    dic['cdr'] = lambda x: x[1:]
    dic['list'] = lambda *elements: list(elements)
    dic['length'] = lambda l: len(l)
    return dic


def find_ref(ref, env):
    if ref in env:
        return env[ref]
    else:
        raise StandardError(ref + ' not found!')


def eval(x, env):
    if type(x) == str:  # referencia a variavel
        return find_ref(x, env)
    elif type(x) == int or type(x) == float:  # literal
        return x
    elif x[0] == 'define':  # definicao
        [_, var, exp] = x
        env[var] = eval(exp, env)
    else:  # chamada de funcao
        proc = eval(x[0], env)
        args = [eval(arg, env) for arg in x[1:]]
        return proc(*args)


def formatted(exp):
    # exibe saida na forma usual do scheme.
    # Ex: [1,2,3] eh impresso como (1 2 3)
    if type(exp) == list:
        return '(' + ' '.join([formatted(e) for e in exp]) + ')'
    else:
        return str(exp)


def scheme(prompt='> '):
    print 'Minimum scheme interpreter'
    print 'Type ^C to quit'
    global_env = create_env()  # cria ambiente global
    while True:
        try:
            user_input = get_semantic_tree(raw_input(prompt))
            val = eval(user_input, global_env)
            if val is not None:
                print(formatted(val))
        except KeyboardInterrupt:
            print 'Bye!'
            return
        except Exception as e:  # exibe mensagem da excecao, caso ocorra
            print '%s: %s' % (type(e).__name__, e)
        if __name__ == '__main__':
            scheme()
