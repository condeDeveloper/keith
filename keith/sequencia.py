# -*- coding: utf-8 -*-
"""Numeros de Keith.

Pegue os digitos de um numero e trate-os como o comeco de uma sequencia tipo
Fibonacci: cada termo novo e a soma dos n anteriores, onde n e a quantidade de
digitos. Se o proprio numero aparecer na sequencia, ele e um numero de Keith.

    197 ->  1, 9, 7, 17, 33, 57, 107, 197        aparece!
     14 ->  1, 4, 5, 9, 14                       aparece!
     15 ->  1, 5, 6, 11, 17, 28                  passou direto

Eles sao raros de um jeito desconfortavel: existem apenas 36 abaixo de dez
milhoes, e a busca inteira ja feita no mundo achou pouco mais de cem.

A sequencia cresce rapido — cada termo e quase o dobro do anterior — entao o
teste de um numero termina em poucas dezenas de passos. O que nao termina
rapido e a varredura: nao se conhece jeito de achar um numero de Keith sem
testar numero por numero, e este repositorio mede exatamente o preco disso.
"""


def digitos_de(n):
    if n < 0:
        raise ValueError('n nao pode ser negativo: %r' % (n,))
    return [int(c) for c in str(n)]


def gerar(n, passos):
    """A sequencia de Keith de n, com ``passos`` termos alem dos digitos."""
    janela = digitos_de(n)
    saida = list(janela)
    for _ in range(passos):
        novo = sum(janela)
        saida.append(novo)
        janela = janela[1:] + [novo]
    return saida


def cadeia_ate(n):
    """A sequencia de n, parando quando passar do proprio n.

    Devolve a lista inteira, incluindo o termo que alcancou ou passou.
    """
    janela = digitos_de(n)
    if len(janela) < 2:
        return list(janela)
    saida = list(janela)
    while saida[-1] < n:
        novo = sum(janela)
        saida.append(novo)
        janela = janela[1:] + [novo]
    return saida


def eh_keith(n):
    """True se n aparece na propria sequencia.

    Numeros de um digito nao contam: a sequencia deles comecaria no proprio
    numero, o que tornaria a definicao trivial.
    """
    if n < 10:
        return False
    return cadeia_ate(n)[-1] == n


def passos_ate(n):
    """Quantos termos a sequencia produz antes de alcancar ou passar n."""
    if n < 10:
        return 0
    return len(cadeia_ate(n)) - len(digitos_de(n))
