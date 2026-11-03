# -*- coding: utf-8 -*-
"""Varre os inteiros procurando numeros de Keith, e confere os dois caminhos."""
from . import juiz, sequencia


def ate(limite):
    """Todos os numeros de Keith de 10 ate o limite."""
    if limite < 10:
        raise ValueError('limite pequeno demais: %r' % (limite,))
    return [n for n in range(10, limite + 1) if sequencia.eh_keith(n)]


def conferir_contra_juiz(limite):
    """Compara a janela que para cedo com a lista que guarda tudo.

    Devolve quantos numeros foram conferidos.
    """
    conferidos = 0
    for n in range(10, limite + 1):
        pela_janela = sequencia.eh_keith(n)
        pela_lista = juiz.eh_keith(n)
        if pela_janela != pela_lista:
            raise AssertionError(
                'os dois caminhos discordam em %d: janela %s, lista %s'
                % (n, pela_janela, pela_lista))
        conferidos += 1
    return conferidos


def conferir_sequencias(numeros):
    """Confere que cada termo e mesmo a soma dos n anteriores."""
    passos = 0
    for n in numeros:
        c = sequencia.cadeia_ate(n)
        largura = len(sequencia.digitos_de(n))
        for i in range(largura, len(c)):
            if c[i] != sum(c[i - largura:i]):
                raise AssertionError(
                    'na sequencia de %d o termo %d nao e a soma dos %d anteriores'
                    % (n, i, largura))
            passos += 1
        if c[-1] != n:
            raise AssertionError('a sequencia de %d nao terminou nele mesmo' % n)
    return passos


def por_quantidade_de_digitos(limite):
    """Quantos numeros de Keith existem com cada quantidade de digitos."""
    conta = {}
    for n in ate(limite):
        d = len(str(n))
        conta[d] = conta.get(d, 0) + 1
    return conta


def passos_dos_achados(numeros):
    """Quantos passos cada numero de Keith leva para se alcancar."""
    return [(n, sequencia.passos_ate(n)) for n in numeros]


def densidade_por_faixa(limite, faixas=7):
    """Quantos numeros de Keith por faixa, para ver a raridade crescer."""
    achados = ate(limite)
    tamanho = limite // faixas
    linhas = []
    for f in range(faixas):
        baixo = f * tamanho + 1
        alto = baixo + tamanho - 1
        dentro = [n for n in achados if baixo <= n <= alto]
        linhas.append((baixo, alto, len(dentro), dentro))
    return linhas


def custo_de_decidir(limite, amostra=1000):
    """Quantos termos, em media, sao precisos para decidir um numero.

    Mostra que o teste de UM numero e barato: o caro e haver muitos numeros.
    """
    passo = max(1, limite // amostra)
    total = 0
    quantos = 0
    for n in range(10, limite + 1, passo):
        total += sequencia.passos_ate(n)
        quantos += 1
    return total / quantos, quantos
