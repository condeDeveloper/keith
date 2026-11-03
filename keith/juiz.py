# -*- coding: utf-8 -*-
"""O juiz: constroi a sequencia inteira guardando tudo, e procura o numero
nela com uma busca linear.

O caminho principal usa uma JANELA de n termos e para assim que passa do
numero. Este guarda a lista toda, gera uma quantidade fixa de termos e depois
procura. Gasta memoria e tempo a toa — e nao tem como errar por parar cedo
demais, que e o risco do outro.
"""
from . import sequencia


def eh_keith(n, passos=200):
    """True se n aparece entre os primeiros ``passos`` termos da sequencia."""
    if n < 0:
        raise ValueError('n nao pode ser negativo: %r' % (n,))
    if n < 10:
        return False
    todos = sequencia.gerar(n, passos)
    # os digitos iniciais nao contam: a busca comeca depois deles
    return n in todos[len(sequencia.digitos_de(n)):]


def varrer(baixo, alto):
    """Todos os numeros de Keith no intervalo, pelo caminho que guarda tudo."""
    if baixo < 0 or alto < baixo:
        raise ValueError('intervalo invalido: %r a %r' % (baixo, alto))
    return [n for n in range(baixo, alto + 1) if eh_keith(n)]


def quantos_termos_bastam(n):
    """Quantos termos sao suficientes para decidir n.

    A sequencia cresce pelo menos como as potencias de dois a partir de certo
    ponto, entao o numero de termos necessarios e proporcional ao numero de
    BITS de n, e nao a n.
    """
    return n.bit_length() + len(sequencia.digitos_de(n))
